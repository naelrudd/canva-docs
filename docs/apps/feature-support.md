Source: https://www.canva.dev/docs/apps/feature-support/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Feature support

How apps can adapt to their current context.

Apps can run in different contexts. For example, apps can run in different [design types](https://www.canva.dev/docs/apps/designs/), such as presentations and documents, and on different surfaces, such as the object panel and selected image overlays.

Some features of the Apps SDK, however, are only available in certain contexts.

## What affects feature support?

Whether or not a feature is supported in the current context depends on a variety of factors, including:

* The design type of the current design.
* The surface on which the app is mounted.

In the future, additional factors may be introduced.

## Checking if a feature is supported

Something we want to avoid is requiring apps to implement complex logic to determine whether or not a feature is available in the current context. As much as possible, we want to abstract away this complexity.

To allow for this, we've included a `useFeatureSupport` hook in the starter kit:

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtCursor, addElementAtPoint } from "@canva/design";
import { useFeatureSupport } from "@canva/app-hooks";
import * as styles from "styles/components.css";

export const App = () => {
  const isSupported = useFeatureSupport();
  const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
    isSupported(fn),
  );

  function handleClick() {
    addElement?.({
      type: "text",
      children: ["Hello world"],
    });
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!addElement}
          tooltipLabel={
            !addElement ? "This feature is not supported in the current page" : undefined
          }
        >
          Add element
        </Button>
      </Rows>
    </div>
  );
};
```

This hook returns an `isSupported` function that:

* Accepts a method as its only argument.
* Returns `true` if the specified method is available in the current context.

By using this function:

* You don't have to think about the conditional logic. It's "invisible" to the app.
* Your app will automatically adapt if the conditional logic changes.

Any method *can* be checked for compatibility, but only some methods need checking. To learn which methods need to be checked, see the [Feature support matrix](https://www.canva.dev/#feature-support-matrix).

**Note:** Under the hood, the `useFeatureSupport` hook calls methods from the `@canva/platform` package. Where possible though, we strongly encourage developers to use the hook.

## Checking if feature support changes

In the future, there will be situations where the availability of a feature may change while an app is open. If you're using the `useFeatureSupport` hook, this isn't something you need to think about, as the `isSupported` function is reactive and automatically listens for these changes.

If you're not using the hook though, you'll need to register a callback that listens for these changes:

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtCursor, addElementAtPoint } from "@canva/design";
import type { Feature } from "@canva/platform";
import { features } from "@canva/platform";
import { useEffect, useState } from "react";
import * as styles from "styles/components.css";

export const App = () => {
  const [isSupported, setIsSupported] = useState(() => {
    return (...args: Feature[]) => features.isSupported(...args);
  });

  // Listen for feature support changes
  useEffect(() => {
    return features.registerOnSupportChange(() => {
      setIsSupported(() => {
        return (...args: Feature[]) => features.isSupported(...args);
      });
    });
  }, []);

  const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
    isSupported(fn),
  );

  function handleClick() {
    addElement?.({
      type: "text",
      children: ["Hello world"],
    });
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!addElement}
          tooltipLabel={
            !addElement ? "This feature is not supported in the current page" : undefined
          }
        >
          Add element
        </Button>
      </Rows>
    </div>
  );
};
```

Apps are only properly compatible with different contexts if they listen for these changes.

## TypeScript considerations

The `useFeatureSupport` hook isn't type-safe. The same is true for the methods it calls. This is because features are checked for compatibility at runtime, not at compile time.

This is important because it means that **an app compiling without TypeScript errors isn't a guarantee that the app will run in the browser**.

Therefore, we recommend:

* Manually testing your app in a variety of contexts, such as in different design types.
* Not relying on type-checking to catch feature compatibility errors.

## Feature support matrix

This section lists all of the context-sensitive methods in the Apps SDK.

You can use this information to:

* Identify when you need to use the `useFeatureSupport` hook.
* Identify when you need to test your app in different contexts.

Only context-sensitive methods are shown in this table. If a method isn't listed in the table, assume that it's available in all contexts. Additionally, this table doesn't show deprecated methods.
