Source: https://www.canva.dev/docs/apps/app-configuration/collaboration/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Collaboration

How to collaborate on apps with your team.

App collaboration allows multiple team members to build, test, and manage apps together in the Developer Portal.

## Prerequisites

* You must have a **Canva Teams** or **Canva Enterprise** plan. See [Canva plans](https://www.canva.com/pricing).
* Users must join your Canva team before you can add them as app collaborators. Team admins or owners can invite users from [Canva team settings](https://www.canva.com/settings/people).
* You must be an app owner or manager to add, remove, and edit collaborators.

## Adding collaborators

1. Navigate to your app in the [Developer Portal](https://www.canva.com/developers/apps).
2. Select the **Collaborators** tab.
3. Select **Add collaborators**.
4. Choose the team members you want to add. You can only add collaborators from within your Canva team.

When you add a collaborator, they immediately gain access. They will see the app listed in their [Developer Portal](https://www.canva.com/developers/apps).

## Collaborator roles

There are 3 collaborator roles, listed from lowest to highest privilege:

| Role    | Permissions                                                                                                                                                                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Member  | <ul><li>Can edit **all** app fields (for example, Code upload, App listing details, Your details).</li><li>Can preview the app.</li><li>Can submit the app for review, release it, and create a new version.</li><li>Can view **all** app versions, including previous versions.</li></ul> |
| Manager | <ul><li>All Member permissions.</li><li>Can add and remove collaborators.</li><li>Can change collaborators' roles.</li></ul>                                                                                                                                                               |
| Owner   | <ul><li>All Manager permissions.</li><li>Can delete the app.</li></ul>                                                                                                                                                                                                                     |

## Managing collaborators

You must be an app owner or manager to change roles or remove collaborators.

### Changing collaborator roles

1. Navigate to your app in the [Developer Portal](https://www.canva.com/developers/apps).
2. Select the **Collaborators** tab.
3. Find the collaborator whose role you want to change.
4. Select the drop-down next to their current role.
5. Select the new role.

### Removing collaborators

1. Navigate to your app in the [Developer Portal](https://www.canva.com/developers/apps).
2. Select the **Collaborators** tab.
3. Find the collaborator you want to remove.
4. Select the drop-down next to their current role.
5. Select the **Remove collaborator** option.

When a collaborator is removed, they immediately lose access to the app.

### Transferring ownership

You must be the current app owner to transfer ownership.

1. Navigate to your app in the [Developer Portal](https://www.canva.com/developers/apps).
2. Select the **Collaborators** tab.
3. Find the collaborator you want to make the new owner.
4. Select the drop-down next to their current role.
5. Select the **Owner** option.

After transferring ownership, your role changes to **Manager**.

## Limitations

* There's a maximum of **49** collaborators per app.
* Collaborators don't have access to the JSD support ticket created when submitting an app for review.
* If a team's Canva Teams or Enterprise subscription expires, the app reverts to a single-user app, where only the owner can access it. When the subscription is renewed, all collaborators regain access.
