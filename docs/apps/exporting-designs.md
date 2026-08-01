Source: https://www.canva.dev/docs/apps/exporting-designs/

# Exporting designs

How to export a design from Canva.

Apps can also trigger the export of a user's design and then access the URLs of the exported files.

**Note:** **Canva is currently not accepting public export-only apps.**

## Supported export formats

| Name         | MIME type                     | Common file extensions |
| ------------ | ----------------------------- | ---------------------- |
| GIF          | image/gif                     | .gif                   |
| JPG          | image/jpeg                    | .jpg, .jpeg            |
| MP4 video    | video/mp4                     | .mp4                   |
| PDF Standard | application/pdf               | .pdf                   |
| PNG          | image/png                     | .png                   |
| PPTX         | application/vnd.ms-powerpoint | .pptx                  |
| SVG          | image/svg+xml                 | .svg                   |

## How to export a design

### Step 1: Open an export dialog

```ts
import { requestExport } from "@canva/design";

await requestExport({
  acceptedFileTypes: ["jpg", "png"],
});
```

### Step 2: Download the exported files

```ts
const result = await requestExport({
  acceptedFileTypes: ["jpg", "png"],
});

console.log(result); // => { status: "complete", title: "My design", exportBlobs: [{ url: "https://example.com/image.png" }] }
```

The URL expires after 60 minutes.

#### Handling multi-page designs

File types supporting multiple pages: `"gif"`, `"pdf_standard"`, `"pptx"`, `"video"`.
File types not supporting multiple pages: `"jpg"`, `"png"`, `"svg"`.

### (Optional) Step 3: Handle abandoned exports

```ts
const result = await requestExport({
  acceptedFileTypes: ["jpg", "png"],
});

console.log(result); // => { status: "aborted" }
```

## Known limitations

* Apps must support at least one export file type.
* Apps are limited to 500 exports per user, per day, and 75 exports per user every 5 minutes.
