Source: https://www.canva.dev/docs/connect/changelog/

# Changelog

* **2026-05-27**: The preview Get design pages API now returns a `page_number` property, replacing the deprecated `index` property.
* **2026-05-14**: The Create design API now supports two new creation modes: `type: design` (copying) and `type: brand_template`.
* **2026-05-12**: The Create design export job API now supports CSV export. New preview APIs: Create design merge job and Get design merge job.
* **2026-03-30**: The Create design API now supports `email` in the `name` field for `preset` types.
* **2026-03-26**: A new `type` request parameter added to the Create design API.
* **2026-03-25**: The Create design autofill job API now supports `column_configs` for chart data fields. The Create design export job API now supports `html_bundle` and `html_standalone` email export formats.
* **2026-03-02**: The Assets APIs now return an additional `metadata` property.
* **2026-02-26**: The List folder items API now supports a `pin_status` parameter.
* **2026-02-19**: The Get design pages API now returns page dimensions for bounded designs.
* **2026-01-08**: The Get design export formats API is now generally available.
* **2026-01-05**: The List brand templates API now supports an optional `limit` parameter.
* **2025-12-02**: The List folder items API now supports a `limit` parameter.
* **2025-10-20**: The List designs API now supports a `limit` parameter.
* **2025-08-11**: The folders API now lets you reference a user's Uploads folder using `uploads` as the folder ID.
* **2025-07-02**: New preview APIs: Create asset upload job via URL and Get asset upload job via URL.
* **2025-06-24**: The URL import job APIs are now generally available.
* **2025-06-19**: Video file support in Assets APIs is now generally available. The design Resize APIs are now generally available. The Get user capabilities API is now generally available.
* **2025-05-12**: New restriction on preview comment APIs: messages limited to 2048 characters.
* **2025-03-26**: New preview APIs: Create design resize job and Get design resize job.
* **2025-03-19**: In Suggestion webhook notifications, the `format` property can now have `font_size_modifier` and `vertical_align`.
* **2025-03-17**: The preview Comment notification webhook event now returns a `comment_event` object.
* **2025-02-24**: New preview API: Create reply.
* **2025-02-20**: New preview API: Create thread.
* **2025-02-19**: The Create design export job API now includes a `transparent_background` parameter for PNG exports.
* **2025-02-18**: The Get thread, Get reply and List replies APIs now support the suggestion type.
* **2025-02-17**: Brand template `created_at` and `updated_at` now consistently represent seconds since the UNIX epoch.
* **2025-02-12**: New preview API: List replies.
* **2025-01-17**: New preview API: Get reply. Get comment API renamed to Get thread.
* **2025-01-15**: New preview APIs: Create URL import job and Get URL import job.
* **2025-01-08**: Deleted user mentions in comments now return as `[]`.
* **2025-01-07**: Passing an empty design ID to Create design export job now returns 400 instead of 500.
* **2024-12-17**: The preview Suggestion notification webhook event now contains a suggestion thread with multiple suggested edits.
* **2024-12-02**: The Assets APIs now support video files (preview).
* **2024-11-29**: Folder access requested webhook now returns FolderSummary instead of Folder.
* **2024-11-22**: Share folder webhook now includes `created_at` and `updated_at` timestamps.
* **2024-11-12**: Autofill, Design import, List folder items APIs now return `page_count`. Webhook notifications now return `page_count`.
* **2024-10-25**: New preview API: Get design export formats.
* **2024-10-23**: Suggestion notification webhook events now sent to integrations.
* **2024-10-11**: New preview API: Get design pages.
* **2024-09-19**: Design import and Folders APIs are now generally available.
* **2024-09-18**: List brand templates now supports optional `dataset` query parameter.
* **2024-09-17**: Create design autofill job now accepts `chart` data fields. Get brand template dataset now returns `chart` fields.
* **2024-09-11**: Webhook `created_at` now correctly represents seconds since UNIX epoch.
* **2024-09-05**: Designs APIs now return `page_count`. PNG export `lossless` now defaults to `true`.
* **2024-09-04**: List folder items no longer includes `owner` for designs. `template` item type removed.
* **2024-08-23**: Assets APIs now return an additional `type` property.
* **2024-08-22**: Autofill APIs now return `created_at`, `updated_at`, and temporary URLs.
* **2024-08-16**: Brand template and Designs APIs now return `created_at` and `updated_at` timestamps.
* **2024-07-08**: Autofill and Brand template APIs are now generally available.
* **2024-06-18**: **New API version: 2024-06-18** - Initial release of the Connect APIs.
