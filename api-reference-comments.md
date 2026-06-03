Source: https://www.canva.dev/docs/connect/api-reference/comments/

# Comments

The Canva Connect APIs for design comments.

<Warning>
  The comments APIs are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
  * Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
</Warning>

The `comments` endpoint allows you to create new top-level comments on designs and reply to a top-level comment thread.

## Comments APIs

* [Create thread](https://www.canva.dev/docs/connect/api-reference/comments/create-thread/): Create a new comment thread on a design.
* [Create reply](https://www.canva.dev/docs/connect/api-reference/comments/create-reply/): Reply to a comment on a design.
* [Get thread](https://www.canva.dev/docs/connect/api-reference/comments/get-thread/): Get metadata for a comment thread.
* [Get reply](https://www.canva.dev/docs/connect/api-reference/comments/get-reply/): Get a comment reply.
* [List replies](https://www.canva.dev/docs/connect/api-reference/comments/list-replies/): List replies for a comment on a design.
* <Badge tone="feedbackWarnSubtle">deprecated</Badge> [Create comment](https://www.canva.dev/docs/connect/api-reference/comments/create-comment/): Create a new comment on a design.