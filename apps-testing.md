Source: https://www.canva.dev/docs/apps/testing/

# Unit testing

How to unit test apps with Jest and React Testing Library.

## Recommended tooling

In the [starter kit](https://github.com/canva-sdks/canva-apps-sdk-starter-kit), we've included:
* [Jest](https://jestjs.io/docs/getting-started)
* [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

## Setting up a test environment

1. Update to the latest SDK packages:

   ```bash
   npm install @canva/app-i18n-kit@latest @canva/app-ui-kit@latest @canva/asset@latest @canva/design@latest @canva/error@latest @canva/platform@latest @canva/user@latest
   ```

2. Create `jest.setup.ts`:

   ```tsx
   import * as asset from "@canva/asset/test";
   import * as design from "@canva/design/test";
   import * as error from "@canva/error/test";
   import * as intents from "@canva/intents/test";
   import * as platform from "@canva/platform/test";
   import * as user from "@canva/user/test";

   asset.initTestEnvironment();
   design.initTestEnvironment();
   error.initTestEnvironment();
   intents.initTestEnvironment();
   platform.initTestEnvironment();
   user.initTestEnvironment();

   jest.mock("@canva/asset");
   jest.mock("@canva/design");
   jest.mock("@canva/intents");
   jest.mock("@canva/platform");
   jest.mock("@canva/user");
   ```

## Testing an app's user interface

```tsx
import { render } from "@testing-library/react";
import { TestAppI18nProvider } from "@canva/app-i18n-kit";
import { TestAppUiProvider } from "@canva/app-ui-kit";

function renderInTestProvider(node: React.ReactNode) {
  return render(
    <TestAppI18nProvider>
      <TestAppUiProvider>{node}</TestAppUiProvider>
    </TestAppI18nProvider>
  );
}
```

## Testing an app's behavior

```tsx
const mockRequestOpenExternalUrl = jest.mocked(requestOpenExternalUrl);

it("should open example URL", async () => {
  mockRequestOpenExternalUrl.mockResolvedValue({ status: "completed" });
  const result = renderInTestProvider(<App />);
  const button = result.getByRole("button", { name: "Click here" });
  await fireEvent.click(button);
  expect(requestOpenExternalUrl).toHaveBeenCalled();
});
```

## Running tests

```bash
npm run test
```
