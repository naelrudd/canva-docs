Source: https://www.canva.dev/docs/connect/submission-checklist/

# Submission checklist

What to do before submitting an integration for review.

NOTE: Submitting an integration for review is only required for **Public** integrations.

## Before submission

### Check your email address
Make sure the email address you use to login to Canva is integrated with your external platform.

### Read Canva's terms and conditions
* Terms of Use
* Canva Developer Terms

### Use a suitable hosting platform
Use a hosting platform that's reliable, secure, and capable of handling expected traffic. Don't use free services like Glitch for production.

### Follow Canva's brand guidelines
Any references to Canva on your platform must adhere to Canva's brand guidelines.

### Follow the recommended practices and UI guidelines

### Secure your integration

### Test your integration
Test the following at minimum:
* Core functionality
* Authentication flow (with/without active session, existing/new user)

### Make sure your integration configuration is ready for review
* Integration name is suitable for the public.
* At least one valid authentication redirect URL.
* No local URLs as authentication redirect URLs.
* Valid webhook URL if collaboration:event scope is enabled.
* Valid return URL if Return Navigation is enabled.

## After submission

After submitting your integration for review, a ticket is created to track the review process.

### Provide the required details
When the review ticket is created, you'll be asked to:
* Provide login credentials for testing.
* Provide a video demo of your integration.
* Complete a questionnaire about your integration.

### Duration
The duration depends on the complexity of the integration and the amount of feedback required.

### Updates
Updates and messages from the Canva team are added to your ticket. You'll also receive feedback in the Developer Portal when we approve or reject your integration.
