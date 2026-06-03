Source: https://www.canva.dev/docs/connect/canva-concepts/

# Canva concepts

The Canva Connect APIs let your integration interact with various Canva resources. This article explains key concepts that are useful to know when integrating with Canva.

## Canva Apps

Canva Apps available in the [Canva Apps Marketplace](https://www.canva.com/your-apps/) are developed using the [Canva Apps SDK](/docs/apps). These apps are available to users within the Canva editor.

## Canva integrations

Canva integrations allow third-party app developers to extend key Canva capabilities off-platform. For example, Canva for Slack and Canva for ChatGPT. These integrations interact with Canva using the Canva Connect APIs. An integration is what you develop when using the Canva Connect APIs.

## Assets

Assets, known as Uploads in the Canva UI, are user-upload images, audio tracks, and videos. Assets are stored in the user's Projects along with their designs.

For Connect API endpoints that interact with assets, see the [Assets](https://www.canva.dev/docs/connect/api-reference/assets/) API reference.

## Designs

A design is anything you create in Canva, including:
* Documents
* Presentations
* Print products (T-shirts, mugs, business cards)
* Social media content (Instagram posts)
* Videos
* Websites
* Whiteboards

Most Canva designs are between 40 × 40 pixels and 8,000 × 8,000 pixels and can have multiple pages.

For more information, see the [Designs](https://www.canva.dev/docs/connect/api-reference/designs/), [Design import](https://www.canva.dev/docs/connect/api-reference/design-imports/), and [Design types](https://www.canva.dev/docs/connect/api-reference/design-types/) API references.

## Folders

Folders are a collection of items, such as:
* Other folders.
* Assets (uploaded images, audio, videos).
* Designs (Instagram posts, Presentations, Documents).
* Brand Templates.

When identifying folders, we recommend using the folder's `id`. The top level of the user's content library, Projects, is represented in APIs as a folder with the ID `root`.

For Connect API endpoints that interact with folders, see the [Folders](https://www.canva.dev/docs/connect/api-reference/folders/) API reference.

## Teams, groups, and users

Canva users are organized into *organizations*, *teams*, and *groups*. For Canva Enterprise customers, an Organization is the largest organizational unit. For non-enterprise customers, a Team is the largest organizational unit.

All users are in at least one team (including Canva Free and Canva Pro users). Users in a team have access to all content shared with that team.

Groups belong to a team and can't be shared between two teams.
