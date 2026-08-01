Source: https://www.canva.dev/docs/apps/design-guidelines/errors/

# Errors & messaging

Guidelines for displaying errors and messaging.

## Crafting error messages

The two key components of an error message:

1. **Tell users what went wrong. Be specific, but only when it helps.**

   Vague messages such as "We encountered an unknown error" or "Something went wrong" can be frustrating for users. We should also avoid being too specific, because general users can feel alienated by messages that mention "504 gateway timeout error".

   If you don't know what went wrong, explain what you do know. You can usually say that what the user expected to happen, hasn't happened – for example, "We couldn't load your folders."

2. **Tell them how to fix it (or what to do next).** Let the user know what steps they can take to solve the problem – like trying again, or reloading the page.

## Best practices

### Using error messages

An error message should be a last resort. If a particular action (for example, clicking on a certain button) leads to an error, disable that action instead.

### Avoid jargon

Use language that everyone from a 10-year-old to a grandmother will understand. Technical language may help explain an error to your fellow engineers, but it doesn't help our users.

### Use humor and "cute" words sparingly

Messages that say "whoops!" are fine when a user does something wrong, but when it's a technical problem – like something not saving properly, for example – it looks like this frustrating issue isn't being taken seriously. Creating helpful error messages should be your priority. If you would like to add a bit of humor, make sure it improves the user experience.

### Be positive

Words like "error" and "problem" can fill users with fear. Instead of writing "Bad request. Password is invalid", try something more positive, such as "That password wasn't right. Try again?" Never blame a user for an error.

### Use contractions

For example, use "you're" and "we're". These sound more human and less robotic, which makes error messages seem less scary.

### Avoid exclamation marks

These can make messages seem alarming or frivolous.

## Example errors

### Form and input

### Auth
