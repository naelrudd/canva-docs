Source: https://www.canva.dev/docs/apps/creating-image-overlays/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating image overlays

Using the Apps SDK to support in-place editing for images.

An image overlay is an interactive editing surface that is placed on top of a selected image. They enable users to edit images and preview adjustments to images immediately and in context.

For example, imagine an app that applies effects to an image. Overlays allow the user to select an image in their design, choose an effect via the app, and see an in-place preview of what the effect looks like before applying it.

## Features

* Apps can create image overlays for raster images. (Vector images are not supported.)
* Overlays are compatible with most image content, including image elements and page backgrounds.
* Overlays can receive pointer events, which allows apps to support brush controls.

## Cropping and flipping

In Canva, users can crop and flip images. When a user opens an overlay though:

* Apps can only access the uncropped and unflipped version of the image.
* Apps cannot detect if an image has been cropped or flipped.

This behavior is intentional, but it does have some possibly confusing side effects.

To understand these side effects, imagine an app that adds text to the top-left corner of an image. If the image is not cropped or flipped, the app works as expected.

If the image is cropped before the overlay is opened though, the text may only be partially visible. This is because the text is being added to the entire image, not only the cropped (visible) portion of the image.

If the image is flipped before the overlay is opened, the text will appear upside down, in the bottom-right corner. This is because the text is being added to the original image in its unflipped state.

To account for this behavior, we recommend:

* Testing your apps with images that have been cropped and/or flipped.
* Rendering UI elements in the object panel, not the overlay iframe. (See the [design guidelines](https://www.canva.dev/docs/apps/design-guidelines/overlays/#adding-ui-to-the-overlays).)

## How to create image overlays

### Step 1: Enable the required scopes

In the Developer Portal, enable the following scopes:

* `canva:design:content:read`
* `canva:design:content:write`
* `canva:asset:private:read`
* `canva:asset:private:write`

In the future, the Apps SDK will throw an error if the required scopes aren't enabled.

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 2: Open an overlay

1. Import the `useOverlay` hook from the `@canva/app-hooks` package:

   ```tsx
   import { useOverlay } from "@canva/app-hooks";
   ```

2. Call the hook with an argument of `"image_selection"`:

   ```tsx
   const overlay = useOverlay("image_selection");
   ```

3. Create a function that calls the overlay's `open` method:

   ```tsx
   function handleOpen() {
     overlay.open();
   }
   ```

4. Render a button that, when clicked, calls the `handleOpen` function:

   ```tsx
   return (
     <div className={styles.scrollContainer}>
       <Rows spacing="2u">
         <Button
           variant="primary"
           disabled={!overlay.canOpen}
           onClick={handleOpen}
         >
           Edit image
         </Button>
       </Rows>
     </div>
   );
   ```

5. Use the `canOpen` property to disable the button if the overlay can't be opened:

   ```tsx
   <Button variant="primary" disabled={!overlay.canOpen} onClick={handleOpen}>
     Edit image
   </Button>
   ```

   These are some examples of when an overlay can't be opened:

   * an image isn't selected
   * more than one image is selected
   * an overlay is already open

### Step 3: Check the current surface

To run different code based on where the code is running:

1. Import the `appProcess` object from the `@canva/platform` package:

   ```tsx
   import { appProcess } from "@canva/platform";
   ```

2. Call the `getInfo` method to retrieve the information about the current process:

   ```tsx
   const context = appProcess.current.getInfo();
   ```

3. Use the `surface` property to identify the iframe in which the code is running:

   ```tsx
   if (context.surface === "object_panel") {
     return (
       <div className={styles.scrollContainer}>
         <Rows spacing="2u">
           <Button
             variant="primary"
             disabled={!overlay.canOpen}
             onClick={handleOpen}
           >
             Edit image
           </Button>
         </Rows>
       </div>
     );
   }

   if (context.surface === "selected_image_overlay") {
     return <div>This is the selected image overlay.</div>;
   }
   ```

For the sake of readability, extract the code for each surface into separate components.

### Step 4: Check if an overlay is open

To keep track of whether or not an overlay is open, use the `isOpen` property that's returned by the `useOverlay` hook:

```tsx
if (overlay.isOpen) {
  return <div className={styles.scrollContainer}>The overlay is open.</div>;
}

return (
  <div className={styles.scrollContainer}>
    <Rows spacing="2u">
      <Button
        variant="primary"
        disabled={!overlay.canOpen}
        onClick={handleOpen}
      >
        Edit image
      </Button>
    </Rows>
  </div>
);
```

### Step 5: Close the overlay

When the overlay is open, render buttons that each call a function. In each function, call the `close` method that's returned by the `useOverlay` hook:

```tsx
function handleSave() {
  overlay.close({ reason: "completed" });
}

function handleClose() {
  overlay.close({ reason: "aborted" });
}
```

The `reason` property indicates why the overlay is being closed.

### Step 6: Render the selected image

Use the `useSelection` hook and `getTemporaryUrl` method to download and render the selected image within the overlay.

The code for the `SelectedImageOverlay` component:

```tsx
function SelectedImageOverlay() {
  const selection = useSelection("image");
  const canvasRef = React.useRef<HTMLCanvasElement>(null);

  React.useEffect(() => {
    const initializeCanvas = async () => {
      const draft = await selection.read();
      const [image] = draft.contents;

      if (!image) {
        return;
      }

      const { url } = await getTemporaryUrl({ type: "image", ref: image.ref });
      const img = await downloadImage(url);
      const { width, height } = img;

      const { canvas, context } = getCanvas(canvasRef.current);
      canvas.width = width;
      canvas.height = height;
      context.drawImage(img, 0, 0, width, height);

      appProcess.broadcastMessage({ isImageReady: true });
    };

    initializeCanvas();
  }, [selection]);

  return <canvas ref={canvasRef} style={{ width: "100%", height: "100%" }} />;
}
```

### Step 7: Transform the selected image

Broadcast messages between iframes using `appProcess.broadcastMessage` and `appProcess.registerOnMessage`.

### Step 8: Save the user's changes

Use `appProcess.current.setOnDispose` to detect when the overlay closes, then upload the transformed image and replace the original.

### Disabled APIs

Some APIs are disabled within the `"selected_image_overlay"` surface, including:

* `@canva/asset` - `requestFontSelection`
* `@canva/design` - `overlay.registerOnCanOpen`, `requestExport`, `ui.startDrag`, `ui.startDragToPoint`, `ui.startDragToCursor`
* `@canva/user` - `auth.requestAuthentication`

### Gotchas

* An overlay's iframe must adhere to the same [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/) as the rest of the app.
* Overlays are only compatible with image content, such as [image elements](https://www.canva.dev/docs/apps/creating-images/) or page backgrounds.
* Overlays are not compatible with vector images. If a vector image is selected, `canOpen` will be `false`.
* Overlays are not compatible with [app elements](https://www.canva.dev/docs/apps/creating-app-elements/).
