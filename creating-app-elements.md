Source: https://www.canva.dev/docs/apps/creating-app-elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating app elements

How to create app elements.

Once an app adds elements to a user's design, such as [images](https://www.canva.dev/docs/apps/creating-images/) or [videos](https://www.canva.dev/docs/apps/creating-videos/), the app can't edit those elements — it's as if they become invisible to the app.

Sometimes, this can be limiting.

For example, imagine an app that creates gradients. If the app creates the gradients as images, the user can't change the gradient once it exists. They can only create new gradients. To update a gradient:

* The user has to delete the previous gradient from their design.
* A new image has to be uploaded to the user's media library.

This is a sub-par user experience that *app elements* are designed to solve.

## What are app elements?

App elements are a type of element that apps can modify after the element exists in the user's design. They have limitations and a more complex lifecycle, so it doesn't always make sense to use them, but if you're otherwise unable to create the app you want, app elements may be the answer.

Behind the scenes, app elements are groups of elements that:

* Can't be un-grouped — that is, they're *locked* groups
* Can have metadata attached to them

Like [groups](https://www.canva.dev/docs/apps/grouping-elements/), app elements can be made up of multiple child elements, but unlike groups, app elements are allowed to contain a single element.

By attaching metadata to an element, the element's settings — for example, the colors of a gradient — can be persisted on the element itself. The app can update the metadata, causing the element to re-render. The end result is that the elements can be edited by the app that created them.

## How to create app elements

### Step 1: Enable the required scopes

In the Developer Portal, enable the following scopes:

* `canva:design:content:read`
* `canva:design:content:write`

In the future, the Apps SDK will throw an error if the required scopes aren't enabled.

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 2: Define the app element's data structure

Create a type that represents data required to render the element. For example, for an app element to render a gradient, an appropriate type would need to hold at least two colors:

```ts
type AppElementData = {
  color1: string;
  color2: string;
};
```

The name of the type is not important.

### Step 3: Initialize the app element

Import the `initAppElement` method and `AppElementOptions` type from the `@canva/design` package:

```ts
import { AppElementOptions, initAppElement } from "@canva/design";
```

Then call the method **outside of a React component**:

```ts
const appElementClient = initAppElement<AppElementData>({
  render: (data) => {
    const dataUrl = createGradient(data.color1, data.color2);
    return [
      {
        type: "image",
        dataUrl,
        width: 640,
        height: 360,
        top: 0,
        left: 0,
        altText: {
          text: "A gradient background",
          decorative: false,
        },
      },
    ];
  },
});
```

There's a few things going on here, so to break it down:

* The `initAppElement` method should be called outside of a React component because the rendering of the element is not tied to the rendering of the component.
* The type for the app element data is passed to the `initAppElement` method as a type argument. This ensures accurate type information while working with the method.
* The `initAppElement` method accepts an object as its only parameter. This object requires a `render` function that determines the elements to render in the app element. It receives the app element data as its only argument and must return one or more elements.
* The returned elements must have positional properties, including coordinates and dimensions. To learn more about these options, see [Positioning elements](https://www.canva.dev/docs/apps/positioning-elements/).
* The `render` method should only rely on data that's passed in through the `data` parameter. Given the same data, it should return the same result.

In this particular example, the data is passed into the following `createGradient` function that returns a data URL for a gradient. Add the following function after the React component to create a gradient image:

```ts
function createGradient(color1: string, color2: string): string {
  const canvas = document.createElement("canvas");

  canvas.width = 640;
  canvas.height = 360;

  const ctx = canvas.getContext("2d");

  if (!ctx) {
    throw new Error("Can't get CanvasRenderingContext2D");
  }

  const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);

  gradient.addColorStop(0, color1);
  gradient.addColorStop(1, color2);

  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  return canvas.toDataURL();
}
```

### Step 4: Create a type for the app element change event

Create a type that represents the app element change event:

```ts
type AppElementChangeEvent = {
  data: AppElementData;
  update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
};
```

This type includes:

* The data that can be stored on the app element
* An optional update function to handle app element updates

### Step 5: Add the app element's data

To add an app element, start by creating a variable for the app element state within the React component:

```ts
const [state, setState] = React.useState<AppElementChangeEvent>({
  data: {
    color1: "",
    color2: "",
  },
});
```

Then, in a `useEffect` hook, register a callback with the `registerOnElementChange` method:

```ts
React.useEffect(() => {
  appElementClient.registerOnElementChange((element) => {
    if (element) {
      setState({
        data: {
          color1: element.data.color1,
          color2: element.data.color2,
        },
        update: element.update,
      });
    } else {
      setState({
        data: {
          color1: "",
          color2: "",
        },
      });
    }
  });
}, []);
```

This callback runs when:

* A user selects an app element
* A user changes or updates an app element's data
* A user deselects an app element

The callback receives an `element` parameter. When an element is selected, `element` contains a value. Otherwise, it's `undefined`. You can use this behavior to update the state and keep the UI in sync with the user's selection.

### Step 6: Handle element updates

Create a function to handle element updates:

```ts
function handleClick() {
  if (state.update) {
    state.update({
      data: state.data,
    });
  } else {
    appElementClient.addElement({
      data: state.data,
    });
  }
}

function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
  setState((prevState) => {
    return {
      ...prevState,
      data: {
        ...prevState.data,
        [event.target.name]: event.target.value,
      },
    };
  });
}
```

The `handleClick` function does the following:

* If an element is selected, it uses the `update` function, if it exists.
* If an element isn't selected, it creates a new element.

When the user changes input values, the `handleChange` function updates the state .

### Step 7: Create the UI

Create a UI that lets users interact with the app element:

```tsx
return (
  <div>
    <div>
      <input
        type="text"
        name="color1"
        value={state.data.color1}
        placeholder="Color #1"
        onChange={handleChange}
      />
    </div>
    <div>
      <input
        type="text"
        name="color2"
        value={state.data.color2}
        placeholder="Color #2"
        onChange={handleChange}
      />
    </div>
    <button type="submit" onClick={handleClick}>
      {state.update ? "Update" : "Add"}
    </button>
  </div>
);
```

**Warning:** The maximum amount of data that can be attached to an app element is 5 KB.

## Known limitations

* Users can't apply effects to app elements or the elements within them.
* Users can't select the individual elements within an app element.
* Users can't un-group the elements within an app element.
* App elements can only be edited via the apps that created them.
* App elements can't contain groups, tables, videos, or other app elements.
* The maximum amount of data that can be attached to an app element is 5 KB.

## API reference

* [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/)

## Code sample

```tsx
import React from "react";
import { AppElementOptions, initAppElement } from "@canva/design";

type AppElementData = {
  color1: string;
  color2: string;
};

type AppElementChangeEvent = {
  data: AppElementData;
  update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
};

const appElementClient = initAppElement<AppElementData>({
  render: (data) => {
    const dataUrl = createGradient(data.color1, data.color2);
    return [
      {
        type: "image",
        dataUrl,
        width: 640,
        height: 360,
        top: 0,
        left: 0,
        altText: {
          text: "A gradient background",
          decorative: false,
        },
      },
    ];
  },
});

export function App() {
  const [state, setState] = React.useState<AppElementChangeEvent>({
    data: {
      color1: "",
      color2: "",
    },
  });

  React.useEffect(() => {
    appElementClient.registerOnElementChange((element) => {
      if (element) {
        setState({
          data: {
            color1: element.data.color1,
            color2: element.data.color2,
          },
          update: element.update,
        });
      } else {
        setState({
          data: {
            color1: "",
            color2: "",
          },
        });
      }
    });
  }, []);

  function handleClick() {
    if (state.update) {
      state.update({
        data: state.data,
      });
    } else {
      appElementClient.addElement({
        data: state.data,
      });
    }
  }

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    setState((prevState) => {
      return {
        ...prevState,
        data: {
          ...prevState.data,
          [event.target.name]: event.target.value,
        },
      };
    });
  }

  return (
    <div>
      <div>
        <input
          type="text"
          name="color1"
          value={state.data.color1}
          placeholder="Color #1"
          onChange={handleChange}
        />
      </div>
      <div>
        <input
          type="text"
          name="color2"
          value={state.data.color2}
          placeholder="Color #2"
          onChange={handleChange}
        />
      </div>
      <button type="submit" onClick={handleClick}>
        {state.update ? "Update" : "Add"}
      </button>
    </div>
  );
}

function createGradient(color1: string, color2: string): string {
  const canvas = document.createElement("canvas");

  canvas.width = 640;
  canvas.height = 360;

  const ctx = canvas.getContext("2d");

  if (!ctx) {
    throw new Error("Can't get CanvasRenderingContext2D");
  }

  const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);

  gradient.addColorStop(0, color1);
  gradient.addColorStop(1, color2);

  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  return canvas.toDataURL();
}
```
