Source: https://www.canva.dev/docs/apps/app-ui-kit/

# App UI Kit

What is the App UI Kit? Why use it?

The App UI Kit is a React-based component library designed for creating apps that emulate Canva's look and feel. If you're using the [starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/), the App UI Kit is already installed. Otherwise, refer to [the Quickstart guide](https://www.canva.dev/docs/apps/app-ui-kit/quickstart/).

## Features

* Based on the components used by Canva's own engineers.
* Designed for accessibility, usability, and cross-platform compatibility.
* Includes a variety of [icons](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-icons-icons--docs) and [design tokens](https://www.canva.dev/docs/apps/app-ui-kit/design-tokens/).

## When to use

We **strongly** recommend using the App UI Kit if you're planning to release an app to the public, because this makes it easier to comply with our [design guidelines](https://www.canva.dev/docs/apps/design-guidelines/). Without these components, meeting the guidelines can be challenging.

If you're developing an app solely for your team members, using the App UI Kit will provide a more familiar user experience, although it's not mandatory.

## Example

```tsx
import React from "react";
import { Button, Rows, Text, Title } from "@canva/app-ui-kit";

export function App() {
  return (
    <Rows spacing="2u">
      <Rows spacing="1u">
        <Title>Hello world</Title>
        <Text>This is a paragraph of text.</Text>
      </Rows>
      <Button variant="primary">Click me</Button>
    </Rows>
  );
}
```

## Live playground 🎉

To play around with the App UI Kit components, check out the [App UI Kit Playroom](https://playroom.canva.dev/app-ui-kit/) — a live playground that comes preloaded with all of the UI components and examples of how to use them.
