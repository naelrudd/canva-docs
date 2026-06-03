Source: https://www.canva.dev/docs/apps/verifying-jwts/

# JSON Web Tokens

How to verify a JSON Web Token (JWT).

**Danger:** Apps must only verify JWTs through the app's backend — never through the frontend.

## Types of tokens

* **Design tokens** - Encode information about the current design (`aud`, `designId`).
* **User tokens** - Encode information about the current user (`aud`, `brandId`, `userId`).

## Verifying JWTs with @canva/app-middleware

```shell
npm install @canva/app-middleware
```

## Manually verifying JWTs

### Step 4: Verify the token

```ts
const verified = jwt.verify("JWT_GOES_HERE", publicKey, {
  audience: "YOUR_APP_ID",
});
```

### Design tokens

```tsx
if (!verified.aud || !verified.designId) {
  throw new Error("The design token is not valid");
}
```

### User tokens

```tsx
if (!verified.aud || !verified.brandId || !verified.userId) {
  throw new Error("The user token is not valid");
}
```
