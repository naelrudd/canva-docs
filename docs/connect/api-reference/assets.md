Source: https://www.canva.dev/docs/connect/api-reference/assets/

# Assets

The Canva Connect APIs for managing assets.

The `assets` endpoint lets you upload assets to a user's Canva library. You can directly upload assets from the user's local storage system, name and tag the assets, get information about the assets, or update and delete assets using this endpoint.

The `assets` APIs support images and videos.

## Images

Image files must be smaller than 50 MB. Supported formats:
* JPEG
* PNG
* HEIC
* Single-frame GIFs
* TIFF
* Single-frame WEBP

## Videos

Video files must be smaller than 500 MB. Supported formats:
* M4V
* Matroska (MKV)
* MP4 video
* MPEG
* QuickTime
* WebM

## Assets APIs

* [Create asset upload job](https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/): Create an asynchronous job to upload an asset.
* [Get asset upload job](https://www.canva.dev/docs/connect/api-reference/assets/get-asset-upload-job/): Get the status and results of an upload asset job.
* [Create asset upload job via URL](https://www.canva.dev/docs/connect/api-reference/assets/create-url-asset-upload-job/): Create an asynchronous job to upload an asset from a URL.
* [Get asset upload job via URL](https://www.canva.dev/docs/connect/api-reference/assets/get-url-asset-upload-job/): Get the status and results of job to upload asset from a URL.
* [Get asset](https://www.canva.dev/docs/connect/api-reference/assets/get-asset/): Get the metadata for an asset.
* [Update asset](https://www.canva.dev/docs/connect/api-reference/assets/update-asset/): Update the metadata for an asset.
* [Delete asset](https://www.canva.dev/docs/connect/api-reference/assets/delete-asset/): Delete an asset from the user's Projects.
