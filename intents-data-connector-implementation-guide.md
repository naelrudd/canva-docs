Source: https://www.canva.dev/docs/apps/intents/data-connector/implementation-guide/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Connector intent implementation guide

Import data from external sources into Canva.

This guide helps you implement the [Data Connector intent](https://www.canva.dev/docs/apps/intents/data-connector/) to import data from external sources into Canva.

## Quickstart

To get a Data Connector up and running as quickly as possible, we recommend scaffolding a project with the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/) and using the Data Connector template:

```bash
canva apps create my-data-connector --template data_connector
```

This template includes all of the essential boilerplate code to get started.

You can also view a complete working example of a data connector in the [Canva Apps SDK Starter Kit](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/intents/data_connector_intent). This example is deliberately simpler than the CLI template, making it ideal for understanding the core concepts before building more complex implementations.

## Creating a Data Connector

### Step 1: Enable the intent

Before an intent can be implemented, it must be enabled. Enabling an intent informs Canva of when and where the app should be invoked throughout the user experience.

You can configure intents for your app with either the Developer Portal or the Canva CLI:

<Tabs storageKey="configuration">
  <Tab name="Developer Portal">
    1. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page.
    2. On the **Intents** page, find the "Available intents" section.
    3. For the "Data Connector" intent, click **Set up**.
    4. In the "Implement in your code" dialog that appears, click **Done**. The following sections in this guide will walk you through implementing the intent in your code.
  </Tab>

  <Tab name="Canva CLI">
    1. Set up your app to use the Canva CLI to manage settings via the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.
    2. Set the `intent.data_connector` property to be enrolled. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#intent-optional).

       For example, the following enables the Data Connector intent.

       ```json
       {
         "intent": {
           "data_connector": {
             "enrolled": true
           }
         }
       }
       ```
  </Tab>
</Tabs>

### Step 2: Enable the required scopes

In the Apps SDK, certain methods require certain scopes to be enabled. If an app attempts to call methods without the required scopes being enabled, the SDK will throw an error.

The Data Connector intent requires the following scopes:

* **Design read (`canva:design:content:read`)**
* **Design write (`canva:design:content:write`)**

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 3: Register the intent

Before an intent can be implemented, it must be registered. Registering the Data Connector intent establishes how data is fetched and what UI to display for selecting and filtering data.

To register the intent, call the `prepareDataConnector` method as soon as the app loads:

```tsx
import { prepareDataConnector } from "@canva/intents/data";

// Register the data connector when your app loads
prepareDataConnector({
  getDataTable: async (request) => {
    // Return the data table based on the data source reference
    return {
      status: "completed",
      dataTable: {
        rows: [],
      },
    };
  },
  renderSelectionUi: (request) => {
    // Render your selection UI here
    console.log("Rendering selection UI");
  },
});
```

**Note:** Intents must only be registered once. To learn more, see [Technical requirements](https://www.canva.dev/docs/apps/intents/#technical-requirements).

### Step 4: Render the data selection UI

When a user initiates a data import flow, the intent must render a UI that allows the user to select and filter the data that will be imported.

To accomplish this, use the `renderSelectionUi` method:

```tsx
import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { AppI18nProvider } from "@canva/app-i18n-kit";
import {
  AppUiProvider,
  Rows,
  Select,
  FormField,
  Button,
} from "@canva/app-ui-kit";
import {
  prepareDataConnector,
  type RenderSelectionUiRequest,
} from "@canva/intents/data";

const categories = [
  { value: "electronics", label: "Electronics" },
  { value: "clothing", label: "Clothing" },
  { value: "food", label: "Food" },
];

function SelectionUI({ updateDataRef, limit }: RenderSelectionUiRequest) {
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [isLoading, setIsLoading] = useState(false);

  const handleImportData = async () => {
    setIsLoading(true);

    await updateDataRef({
      source: selectedCategory,
      title: `${selectedCategory} Products`,
    });

    setIsLoading(false);
  };

  return (
    <Rows spacing="2u">
      <FormField
        label="Category"
        value={selectedCategory}
        control={(props) => (
          <Select
            {...props}
            options={categories}
            onChange={setSelectedCategory}
            placeholder="Select a category"
          />
        )}
      />
      <Button
        variant="primary"
        onClick={handleImportData}
        disabled={!selectedCategory || isLoading}
        loading={isLoading}
      >
        Import data
      </Button>
    </Rows>
  );
}

// Register the data connector
prepareDataConnector({
  renderSelectionUi: (request) => {
    const root = createRoot(document.getElementById("root") as Element);
    root.render(
      <AppI18nProvider>
        <AppUiProvider>
          <SelectionUI {...request} />
        </AppUiProvider>
      </AppI18nProvider>
    );
  },
  getDataTable: async (request) => {
    // We'll implement this in the next steps
    return { status: "completed", dataTable: { rows: [] } };
  },
});
```

This method receives a `request` object that contains properties for rendering the UI and implementing the data import flow.

#### Initiating OAuth inside intents

If your app requires OAuth with a third-party identity provider, initiate the OAuth flow within the intent action. For Data Connector, you can start OAuth from `renderSelectionUi` during UI rendering, or trigger it from an intent action that requires authentication (for example, during `getDataTable`) before performing the operation.

For implementation guidance, see [Initiating OAuth inside intents](https://www.canva.dev/docs/apps/authenticating-users/oauth/#initiating-oauth-inside-intents).

### Step 5: Create a data source reference

When a user selects the data to import, the app must create a *data source reference*. This is an object that contains:

* A `source` string that encodes all of the information needed to identify and retrieve the data
* A user-friendly title to display in Canva (optional)

The following code samples demonstrates how to create a data source reference from a stringified JSON object:

```tsx
import type { DataSourceRef } from "@canva/intents/data";

const dataSourceRef: DataSourceRef = {
  source: JSON.stringify({
    category: "electronics",
    inStock: true,
    maxPrice: 1000,
  }),
  title: "Electronics Under $1000",
};
```

To learn more, see [Data source references](https://www.canva.dev/#data-source-references).

### Step 6: Store the data source reference

An `updateDataRef` method is passed to the data selection UI via the `request` object. This method is used to store the data source reference on Canva's servers, enabling the data to be refreshed later.

The following code sample demonstrates how to use the `updateDataRef` method:

```tsx
import React, { useState } from "react";
import { Button } from "@canva/app-ui-kit";
import type { RenderSelectionUiRequest } from "@canva/intents/data";

function SelectionUI({ updateDataRef }: RenderSelectionUiRequest) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleImportData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const result = await updateDataRef({
        source: "my-data-source-id",
        title: "My Data",
      });

      if (result.status !== "completed") {
        setError("Failed to save data reference");
      }
    } catch {
      setError("Something went wrong");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {error && <div>{error}</div>}
      <Button onClick={handleImportData} loading={isLoading}>
        Import Data
      </Button>
    </>
  );
}
```

### Step 7: Fetch the requested data

When a data source reference is created or updated, the `getDataTable` method is called. This method is responsible for fetching the requested data and returning it as a *data table*.

A data table represents tabular data in Canva. Similar to spreadsheets, they're made up of rows, columns, and cells of different types. Before data can be imported into Canva, it must be converted into this structure.

The following code sample demonstrates how return a data table:

```tsx
import type { GetDataTableRequest, DataTableRow } from "@canva/intents/data";

const PRODUCTS = {
  electronics: [
    { name: "Laptop", price: 999 },
    { name: "Phone", price: 599 },
  ],
  clothing: [
    { name: "T-Shirt", price: 29 },
    { name: "Jeans", price: 79 },
  ],
};

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    // Parse the data source reference
    const category = request.dataSourceRef.source;

    // Get products for the category
    const products = PRODUCTS[category] || [];

    // Convert to data table format
    const rows: DataTableRow[] = products.map((product) => ({
      cells: [
        { type: "string", value: product.name },
        { type: "number", value: product.price },
      ],
    }));

    return {
      status: "completed",
      dataTable: {
        columnConfigs: [
          { name: "Product", type: "string" },
          { name: "Price", type: "number" },
        ],
        rows,
      },
    };
  },
  renderSelectionUi: (request) => {
    // Implementation from previous step
  },
});
```

To learn more, see [Data tables](https://www.canva.dev/#data-tables).

### Step 8: Handle data size limits

Canva enforces size limits on imported data to ensure optimal performance. Your app receives these limits through the `limit` parameter and must respect them in both the selection UI and when fetching data.

#### Handling limits in the selection UI

When rendering your selection UI, use the `limit` parameter to inform users about size constraints and prevent them from selecting datasets that would exceed these limits:

```tsx
import React, { useState } from "react";
import { Alert, Text } from "@canva/app-ui-kit";
import type { RenderSelectionUiRequest } from "@canva/intents/data";

function SelectionUI({ updateDataRef, limit }: RenderSelectionUiRequest) {
  const [selectedDataset, setSelectedDataset] = useState("");
  const [datasetInfo, setDatasetInfo] = useState<{
    rows: number;
    columns: number;
  } | null>(null);

  // Check dataset size when selection changes
  const handleDatasetSelect = async (datasetId: string) => {
    setSelectedDataset(datasetId);

    // Fetch dataset metadata
    const info = await getDatasetInfo(datasetId);
    setDatasetInfo(info);
  };

  const canImport =
    datasetInfo &&
    datasetInfo.rows <= limit.row &&
    datasetInfo.columns <= limit.column;

  return (
    <>
      {/* Dataset selection UI */}

      {datasetInfo && (
        <Text>
          Dataset size: {datasetInfo.rows} rows × {datasetInfo.columns} columns
        </Text>
      )}

      {datasetInfo && !canImport && (
        <Alert tone="warning">
          This dataset exceeds the maximum allowed size of {limit.row} rows and{" "}
          {limit.column} columns. Please select a smaller dataset or apply
          filters to reduce the size.
        </Alert>
      )}

      <Button onClick={handleImport} disabled={!canImport}>
        Import Data
      </Button>
    </>
  );
}
```

#### Handling limits when fetching data

When implementing `getDataTable`, you must ensure the returned data fits within the specified limits. You have two main strategies:

##### Strategy 1: Truncate data to fit

Limit the data to fit within the allowed constraints. This ensures users can always import data, even if it means getting a subset:

```typescript
import type { GetDataTableRequest } from "@canva/intents/data";

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    const { limit, dataSourceRef } = request;

    // Fetch data from your source
    const allData = await fetchDataFromAPI(dataSourceRef.source);

    // Ensure we don't exceed row limits
    const limitedData = allData.slice(0, limit.row);

    // If we have too many columns, select the most important ones
    const selectedColumns = selectMostImportantColumns(
      allData[0],
      limit.column
    );

    // Convert to data table format
    const rows = limitedData.map((item) => ({
      cells: selectedColumns.map((col) => ({
        type: col.type,
        value: item[col.key],
      })),
    }));

    return {
      status: "completed",
      dataTable: {
        columnConfigs: selectedColumns.map((col) => ({
          name: col.name,
          type: col.type,
        })),
        rows,
      },
      metadata: {
        description: `Showing ${limitedData.length} of ${allData.length} rows`,
      },
    };
  },
  renderSelectionUi: (request) => {
    // Implementation
  },
});
```

##### Strategy 2: Return an error for oversized data

Inform users that their data exceeds limits rather than silently truncating it:

```typescript
import type { GetDataTableRequest } from "@canva/intents/data";

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    const { limit, dataSourceRef } = request;

    // Check data size first
    const dataStats = await getDataStatistics(dataSourceRef.source);

    if (
      dataStats.rowCount > limit.row ||
      dataStats.columnCount > limit.column
    ) {
      return {
        status: "app_error",
        message:
          `Your selected data has ${dataStats.rowCount} rows and ${dataStats.columnCount} columns, ` +
          `but the maximum allowed is ${limit.row} rows and ${limit.column} columns. ` +
          `Please apply filters or select a smaller dataset.`,
      };
    }

    // Fetch and return data
    const data = await fetchData(dataSourceRef.source);
    // ... convert to data table format

    return {
      status: "completed",
      dataTable: formattedData,
    };
  },
  renderSelectionUi: (request) => {
    // Implementation
  },
});
```

### Step 9: Handle fetch errors

When fetching data from external sources, things don't always go as planned. The `getDataTable` method provides three specific error types to handle these scenarios gracefully, ensuring users understand what went wrong and how to proceed.

#### Outdated source reference

The `outdated_source_ref` error indicates that a previously valid data source reference can no longer be used. This error triggers a re-selection flow in Canva, prompting users to choose a new data source.

Use this error when:

* The referenced dataset has been deleted
* User scopes have been revoked
* The data structure has changed incompatibly
* A report or resource has been archived
* Required fields no longer exist in the data source

For example:

```typescript
import type { GetDataTableRequest } from "@canva/intents/data";

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    const sourceId = request.dataSourceRef.source;

    // Check if data source still exists
    const exists = await checkDataSourceExists(sourceId);

    if (!exists) {
      return { status: "outdated_source_ref" };
    }

    // Fetch and return data
    const data = await fetchData(sourceId);
    return {
      status: "completed",
      dataTable: formatAsDataTable(data),
    };
  },
  renderSelectionUi: (request) => {
    // Implementation
  },
});
```

#### Remote request failed

The `remote_request_failed` error indicates temporary connectivity issues or API failures. This suggests the user might succeed by trying again later.

Use this error when:

* Network connection fails or times out
* API server returns 5xx errors
* Database connection cannot be established
* Service is temporarily unavailable
* Rate limits are hit at the API level
* DNS resolution fails

For example:

```typescript
import type { GetDataTableRequest } from "@canva/intents/data";

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    try {
      const response = await fetch("/api/data");

      if (response.status >= 500) {
        return { status: "remote_request_failed" };
      }

      const data = await response.json();
      return {
        status: "completed",
        dataTable: formatAsDataTable(data),
      };
    } catch (error) {
      return { status: "remote_request_failed" };
    }
  },
  renderSelectionUi: (request) => {
    // Implementation
  },
});
```

#### App error

The `app_error` type handles application-specific issues with optional custom messages to guide users.

Use this error when:

* Authentication credentials are missing or expired
* Required configuration is incomplete
* User has exceeded usage quotas
* Data is not yet available (e.g., current month's report)
* Invalid parameters were provided
* Account subscription has expired

For example:

```typescript
import type { GetDataTableRequest } from "@canva/intents/data";

prepareDataConnector({
  getDataTable: async (request: GetDataTableRequest) => {
    // Check if user is authenticated
    const isAuthenticated = await checkAuth();

    if (!isAuthenticated) {
      return {
        status: "app_error",
        message: "Please sign in to access your data.",
      };
    }

    // Check usage limits
    const usageRemaining = await checkUsageLimits();

    if (usageRemaining <= 0) {
      return {
        status: "app_error",
        message: "You've reached your monthly data limit.",
      };
    }

    // Fetch data
    const data = await fetchData();
    return {
      status: "completed",
      dataTable: formatAsDataTable(data),
    };
  },
  renderSelectionUi: (request) => {
    // Implementation
  },
});
```

### Step 10: Handle invocation contexts

When the data selection UI is rendered, the `renderSelectionUi` method receives an `invocationContext` object. This object has a `reason` property that indicates why the UI was launched. Your app must handle these different contexts appropriately to provide a seamless user experience.

#### Data selection

This is the standard flow when users are selecting data for the first time or editing a previous selection. If `dataSourceRef` is provided, it indicates an edit flow where the user is modifying their existing data configuration.

These are some examples of when this may occur:

* User clicks to import data for the first time
* User edits an existing data connection
* User wants to change their data selection criteria

For example:

```typescript
import React, { useState, useEffect } from "react";
import type { RenderSelectionUiRequest } from "@canva/intents/data";
import { Title } from "@canva/app-ui-kit";

function SelectionUI({ invocationContext }: RenderSelectionUiRequest) {
  const [category, setCategory] = useState("");

  useEffect(() => {
    if (invocationContext.reason === "data_selection" && invocationContext.dataSourceRef) {
      // Load existing configuration
      const savedCategory = invocationContext.dataSourceRef.source;
      setCategory(savedCategory);
    }
  }, [invocationContext]);

  return (
    <>
      <Title>{invocationContext.dataSourceRef ? "Edit data" : "Select data"}</Title>
      {/* Your selection UI */}
    </>
  );
}
```

#### Outdated source reference

This occurs when `getDataTable` previously returned an `outdated_source_ref` error during a refresh attempt. The data source reference is no longer valid and users need to select new data.

These are some examples of when this may occur:

* The referenced dataset has been deleted from the external system
* User scopes have been revoked
* Required fields or structure have changed

For example:

```typescript
import React from "react";
import { Alert } from "@canva/app-ui-kit";
import type { RenderSelectionUiRequest } from "@canva/intents/data";

function SelectionUI({ invocationContext }: RenderSelectionUiRequest) {
  if (invocationContext.reason === "outdated_source_ref") {
    return (
      <>
        <Alert tone="warning">
          Your data source is no longer available. Please select a new one.
        </Alert>
        {/* Your selection UI */}
      </>
    );
  }

  return <>{/* Normal selection UI */}</>;
}
```

#### App error

This occurs when `getDataTable` returned an `app_error` during a refresh attempt. Your UI should display the error message and help users recover from the specific issue.

These are some examples of when this may occur:

* Authentication credentials are missing or expired
* API quotas or limits have been exceeded
* Required configuration is incomplete
* Temporary issues that users can resolve

For example:

```typescript
import React from "react";
import { Alert, Button } from "@canva/app-ui-kit";
import type { RenderSelectionUiRequest } from "@canva/intents/data";

function SelectionUI({ invocationContext }: RenderSelectionUiRequest) {

  function handleSignIn() {
    // TODO: Implement sign in flow
  }

  if (invocationContext.reason === "app_error") {
    const errorMessage = invocationContext.message || "An error occurred";

    return (
      <>
        <Alert tone="critical">{errorMessage}</Alert>
        {errorMessage.includes("sign in") && (
          <Button onClick={handleSignIn}>Sign in</Button>
        )}
        {/* Your selection UI */}
      </>
    );
  }

  return <>{/* Normal selection UI */}</>;
}
```

### Step 11: Preview the data connector

1. Navigate to the app via the Developer Portal.
2. Click **Preview**.

## Data source references

A data source reference is an object that identifies and describes a specific data source in your external system. When users select data through your app, you create a data source reference that Canva stores and uses for future data refresh operations.

Data source references are made up of two parts:

* `source`: A string containing all information needed to retrieve the data
* `title`: An optional human-readable description shown to users

The `source` string is entirely controlled by your app — you decide what information to store and how to encode it. When Canva needs to refresh the data, it passes this reference back to your `getDataTable` method.

### Creating references with unique identifiers

When your data sources have stable, unique identifiers, a simple string reference provides the most straightforward solution. This approach works well for systems with existing ID-based architectures where additional context isn't needed to retrieve the data.

```typescript
import type { DataSourceRef } from "@canva/intents/data";

const dataSourceRef: DataSourceRef = {
  source: "report-123",
  title: "Q4 Sales Report",
};
```

### Structuring multi-parameter queries with JSON

Complex data queries often require multiple parameters, filters, and configuration options. JSON serialization offers a clean, extensible format for encoding these requirements while maintaining readability and type safety in your application code.

```typescript
import type { DataSourceRef } from "@canva/intents/data";

type DataConfig = {
  reportId: string;
  filters: {
    region: string;
    year: number;
  };
};

const config: DataConfig = {
  reportId: "sales-2024",
  filters: {
    region: "North America",
    year: 2024,
  },
};

const dataSourceRef: DataSourceRef = {
  source: JSON.stringify(config),
  title: "2024 North America Sales",
};
```

### Encoding parameters as URL query strings

URL query string encoding provides a familiar, standardized format that integrates seamlessly with RESTful APIs and existing web infrastructure. This format excels when your backend already expects query parameters or when you need a more compact representation than JSON.

```typescript
import type { DataSourceRef } from "@canva/intents/data";

const params = new URLSearchParams({
  dataset: "customers",
  status: "active",
  limit: "100",
});

const dataSourceRef: DataSourceRef = {
  source: params.toString(), // "dataset=customers&status=active&limit=100"
  title: "Active Customers",
};
```

## Data tables

A data table is Canva's structured format for representing tabular data. Similar to spreadsheets, data tables consist of rows and columns containing typed cells.

Any external data must be converted into this format before it can be imported into Canva.

### Supported data types

Data tables support the following data types:

* Booleans
* Dates
* Media (i.e., images and videos)
* Numbers
* Strings

Each cell in a data table must specify its type and can optionally be empty (undefined). Columns can be configured with a specific type for consistency, or set as `"variant"` to allow mixed types within the same column.

### Creating your first data table

The most straightforward way to create a data table is to define rows containing string values. This approach works well when you need to quickly structure simple text data without additional formatting or type constraints.

```typescript
import type { DataTable } from "@canva/intents/data";

const simpleTable: DataTable = {
  rows: [
    {
      cells: [
        { type: "string", value: "Apple" },
        { type: "string", value: "Fruit" },
      ],
    },
    {
      cells: [
        { type: "string", value: "Carrot" },
        { type: "string", value: "Vegetable" },
      ],
    },
  ],
};
```

### Defining column structure with configurations

Column configurations enhance your data tables by providing meaningful names and enforcing type consistency. This metadata helps both developers and end-users understand the purpose of each column and ensures data validation.

```typescript
import type { DataTable } from "@canva/intents/data";

const tableWithColumns: DataTable = {
  columnConfigs: [
    { name: "Item", type: "string" },
    { name: "Category", type: "string" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "Apple" },
        { type: "string", value: "Fruit" },
      ],
    },
  ],
};
```

### Formatting numeric data with metadata

Number cells support optional formatting metadata that controls how values appear to users. This feature allows you to display currencies, percentages, and other formatted numbers while maintaining the underlying numeric values for calculations.

```typescript
import type { DataTable } from "@canva/intents/data";

const priceTable: DataTable = {
  columnConfigs: [
    { name: "Product", type: "string" },
    { name: "Price", type: "number" },
    { name: "Discount", type: "number" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "Laptop" },
        {
          type: "number",
          value: 999.99,
          metadata: { formatting: "[$$]#,##0.00" }, // Shows as $999.99
        },
        {
          type: "number",
          value: 0.15,
          metadata: { formatting: "0%" }, // Shows as 15%
        },
      ],
    },
  ],
};
```

### Storing temporal data with date cells

Date cells store temporal information as Unix timestamps measured in seconds. This standardized format ensures consistent date handling across different time zones and locales while allowing for precise time tracking.

```typescript
import type { DataTable } from "@canva/intents/data";

const eventTable: DataTable = {
  columnConfigs: [
    { name: "Event", type: "string" },
    { name: "Date", type: "date" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "Launch" },
        {
          type: "date",
          value: Math.floor(new Date("2024-03-15").getTime() / 1000),
        },
      ],
    },
  ],
};
```

### Representing binary states with boolean cells

Boolean cells excel at representing binary choices, feature flags, and on/off states. These cells provide a clear, unambiguous way to track true/false conditions in your data.

```typescript
import type { DataTable } from "@canva/intents/data";

const featureTable: DataTable = {
  columnConfigs: [
    { name: "Feature", type: "string" },
    { name: "Enabled", type: "boolean" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "Dark Mode" },
        { type: "boolean", value: true },
      ],
    },
    {
      cells: [
        { type: "string", value: "Beta Features" },
        { type: "boolean", value: false },
      ],
    },
  ],
};
```

### Managing optional data with empty cells

Real-world data often contains gaps where information is missing or not applicable. Data tables handle this gracefully by allowing any cell type to be empty through undefined values.

```typescript
import type { DataTable } from "@canva/intents/data";

const contactTable: DataTable = {
  columnConfigs: [
    { name: "Name", type: "string" },
    { name: "Email", type: "string" },
    { name: "Phone", type: "string" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "John Doe" },
        { type: "string", value: "john@example.com" },
        { type: "string", value: undefined }, // No phone number
      ],
    },
  ],
};
```

### Implementing flexible schemas with variant columns

Variant columns accommodate scenarios where a single column needs to store different data types across rows. This flexibility proves invaluable when representing heterogeneous data like configuration properties or dynamic attributes.

```typescript
import type { DataTable } from "@canva/intents/data";

const configTable: DataTable = {
  columnConfigs: [
    { name: "Setting", type: "string" },
    { name: "Value", type: "variant" }, // Accepts any type
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "Max Users" },
        { type: "number", value: 100 },
      ],
    },
    {
      cells: [
        { type: "string", value: "Premium" },
        { type: "boolean", value: true },
      ],
    },
    {
      cells: [
        { type: "string", value: "Expires" },
        { type: "date", value: Math.floor(Date.now() / 1000) },
      ],
    },
  ],
};
```

### Incorporating visual content with media cells

Media cells enable data tables to include rich visual content alongside traditional data types. Each media cell can contain multiple images or videos, complete with metadata about dimensions, format, and AI disclosure status. This makes it possible to import product catalogs with demonstration videos, social media content with video previews, or any dataset that combines visual media with structured data.

```typescript
import type { DataTable } from "@canva/intents/data";

const productCatalog: DataTable = {
  columnConfigs: [
    { name: "Product", type: "string" },
    { name: "Images", type: "media" },
  ],
  rows: [
    {
      cells: [
        { type: "string", value: "T-Shirt" },
        {
          type: "media",
          value: [
            {
              type: "image_upload",
              url: "https://example.com/tshirt.jpg",
              thumbnailUrl: "https://example.com/tshirt-thumb.jpg",
              width: 800,
              height: 800,
              mimeType: "image/jpeg",
              aiDisclosure: "none",
            },
          ],
        },
      ],
    },
    {
      cells: [
        { type: "string", value: "Product Demo" },
        {
          type: "media",
          value: [
            {
              type: "video_upload",
              url: "https://example.com/demo.mp4",
              thumbnailUrl: "https://example.com/demo-thumb.jpg",
              width: 1920,
              height: 1080,
              mimeType: "video/mp4",
              durationMs: 30000, // 30 seconds
              aiDisclosure: "none",
            },
          ],
        },
      ],
    },
  ],
};
```

## Security requirements

When developing a data connector, be mindful of the following security requirements:

* Implement robust validation and access controls to prevent bypassing of security measures.
* Validate all data thoroughly to prevent malformed data that could compromise system integrity.
* Sanitize input data to prevent SQL, script, or command injection that could compromise security.
* When handling spreadsheet data, implement controls to prevent malicious formulas from executing.
* Request only necessary scopes to minimize risk from malicious actors impersonating legitimate apps.
* Exercise caution when your connector accesses sensitive information.
* Avoid logging sensitive information.
* Help the user understand that they may have different privacy settings in their data source than in Canva, their data could become accessible to more users via the Canva design, and to maintain appropriate access controls.
