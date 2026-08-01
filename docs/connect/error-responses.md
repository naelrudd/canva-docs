Source: https://www.canva.dev/docs/connect/error-responses/

# Error responses

When an API request fails, an error response is returned that includes a structured error object containing:
* A `code` property with a standardized error code for programmatic error handling.
* A `message` property with a human-readable description.

## Error codes

The following error codes can be returned by the Connect APIs:

* `internal_error`
* `invalid_field`
* `invalid_header_value`
* `permission_denied`
* `too_many_requests`
* `not_found`
* `bad_request_body`
* `bad_http_method`
* `bad_request_params`
* `bad_query_params`
* `user_role_required`
* `endpoint_not_found`
* `endpoint_gone`
* `unsupported_version`
* `invalid_access_token`
* `revoked_access_token`
* `missing_field`
* `missing_scope`
* `invalid_grant`
* `invalid_request`
* `invalid_client`
* `unauthorized_client`
* `unsupported_grant_type`
* `invalid_scope`
* `invalid_basic_header`
* `invalid_file_format`
* `quota_exceeded`
* `unsupported_content_type`
* `request_too_large`
* `folder_not_found`
* `item_in_multiple_folders`
* `asset_not_found`
* `max_limit_reached`
* `permission_not_found`
* `permission_exists`
* `unauthorized_user`
* `user_not_found`
* `group_not_found`
* `app_not_found`
* `app_has_non_draft_versions`
* `invalid_status_transition`
* `translation_validation_failed`
* `content_not_found`
* `doctype_not_found`
* `design_not_found`
* `offset_too_large`
* `page_not_found`
* `design_or_comment_not_found`
* `design_or_thread_not_found`
* `design_type_not_found`
* `team_not_found`
* `comment_not_found`
* `too_many_comments`
* `too_many_replies`
* `message_too_long`
* `thread_not_found`
* `reply_not_found`
* `design_not_fillable`
* `autofill_data_invalid`
* `feature_not_available`
* `license_required`
* `input_unsafe`
* `display_name_unavailable`
* `user_not_managed`

## Troubleshooting common errors

| Error Code | What it means | How to troubleshoot |
|---|---|---|
| `invalid_access_token` | The provided access token is malformed, expired, or invalid. | Check that your access token is correctly formatted and hasn't expired. |
| `permission_denied` | The user doesn't have permission to access the specified resource. | Handle the error and consider notifying the user. |
| `missing_scope` | The access token doesn't include a required scope. | Add the missing scope to your OAuth authorization request. |
| `not_found` | The requested resource doesn't exist or isn't accessible. | Verify the resource ID is correct. |
| `design_not_found` | The specified design doesn't exist or isn't accessible. | Check the design ID is valid. |
| `too_many_requests` | You've exceeded the API rate limits. | Implement exponential backoff and retry logic. |
| `bad_request_body` | The request body is malformed or contains invalid data. | Validate your JSON payload against the API schema. |
| `bad_request_params` | Invalid parameters in the request URL. | Review the endpoint documentation. |
| `invalid_field` | A specific field in your request contains invalid data. | Check the error message for details. |
| `missing_field` | A required field is missing from your request. | Add all required fields as specified in the API documentation. |
| `internal_error` | An unexpected error occurred on Canva's servers. | Retry your request after a brief delay. |
