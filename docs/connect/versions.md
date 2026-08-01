Source: https://www.canva.dev/docs/connect/versions/

# API versions

The Canva Connect APIs are versioned with a date-based version. This allows Canva to make breaking changes to the API without affecting existing integrations.

Whenever a breaking change is made, a new Connect API version is released with a version identifier based on the change date, for example `2024-01-31`. It's anticipated that superseded versions of the API will remain supported for at least 6 months before the old version is deprecated and removed.

For a list of API versions and a log of breaking and non-breaking changes, see the [Changelog](https://www.canva.dev/docs/connect/changelog/).

WARNING: Breaking changes made to APIs and features that are marked as "Beta" or "Preview" won't produce a new API version.

NOTE: The version number included in endpoint paths (the `v1` in `https://api.canva.com/rest/v1/`) is not used for the API versioning described in this article. That version indicator is reserved for any future epoch-level changes where the entire API and its architecture might fundamentally change.

## Breaking vs. non-breaking changes

### Breaking changes

The following are considered breaking changes, which would require the creation of a new API version:
* Changing the required scopes for an API.
* Adding a required request parameter.
* Changing a request parameter from optional to required.
* Changing the default value of a request parameter.
* Updating an optional query or search parameter.
* Removing an enumerated value from a request parameter.
* Removing a request parameter.
* Changing a validation rule for request parameters or response properties.
* Adding an enumerated value to a response property.
* Changing a response property from required to optional.
* Changing response property behavior.
* Removing a response property.
* Changing a Connect API behavior in a way that isn't backwards compatible.
* Changing the HTTP response status code for an API.

### Non-breaking changes

The following are considered non-breaking changes, which wouldn't require the creation of a new API version:
* Adding an optional request parameter.
* Adding an enumerated value to a request parameter.
* Changing a request parameter from required to optional.
* Adding a response property.
* Changing a response property from optional to required.
* Removing an enumerated value from a response property.

## Managing API versions for your integration

NOTE: You'll be able to use a setting in the Canva Developer Portal to control which API version your integration uses by default. The documentation for managing API versions will be provided when this functionality is available.
