Source: https://www.canva.dev/docs/apps/creating-tables/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating tables

How to add tables to a user's design.

Apps can add tables to a user's design. These tables are a type of [element](https://www.canva.dev/docs/apps/elements/), which means users can manipulate them as they would any other kind of element.

NOTE: If you want to bring external data into your designs or keep it in sync, we recommend you use the [Data Connector Intent](https://www.canva.dev/docs/apps/intents/data-connector/) instead of the Tables API. The Tables API is for programmatically managing table data and structure, not for powering in-design data workflows.

## Features

In addition to creating tables, apps can:

* Set the text content of table cells.
* Set the background color of table cells.
* Merge table cells.

## How to create a table

### Step 1: Enable the required scopes

Enable the `canva:design:content:write` scope.

### Step 2: Create a table

Use the `useTable` hook from the `@canva/app-hooks` package:

```tsx
import { useTable } from "@canva/app-hooks";

const tableState = useTable({ rowCount: 2, columnCount: 2 });
const element = tableState.build();
```

### Step 3: Add the table to the design

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtCursor, addElementAtPoint } from "@canva/design";
import { useFeatureSupport, useTable } from "@canva/app-hooks";

export const App = () => {
  const isSupported = useFeatureSupport();
  const tableState = useTable({ rowCount: 2, columnCount: 2 });

  function handleAddElementAtPoint() {
    if (!isSupported(addElementAtPoint)) return;
    const element = tableState.build();
    addElementAtPoint(element);
  }

  function handleAddElementAtCursor() {
    if (!isSupported(addElementAtCursor)) return;
    const element = tableState.build();
    addElementAtCursor(element);
  }

  return (
    <div>
      <Rows spacing="1u">
        <Button variant="primary" disabled={!isSupported(addElementAtPoint)} onClick={handleAddElementAtPoint}>
          Add table element at point
        </Button>
        <Button variant="primary" disabled={!isSupported(addElementAtCursor)} onClick={handleAddElementAtCursor}>
          Add table element at cursor
        </Button>
      </Rows>
    </div>
  );
};
```

## Customizing tables

* **Adding rows:** Modify `tableState.rowCount`.
* **Adding columns:** Modify `tableState.columnCount`.
* **Setting cell content:** Use the `cells` array with `rowPos`, `columnPos`, and `text`.
* **Setting cell background colors:** Use the `cells` array with `rowPos`, `columnPos`, and `fillColor`.
* **Merging rows:** Set `rowSpan` on a cell customization.
* **Merging columns:** Set `colSpan` on a cell customization.

## Known limitations

* Tables can't exist within [app elements](https://www.canva.dev/docs/apps/creating-app-elements/).
* Tables can't exist within [group elements](https://www.canva.dev/docs/apps/grouping-elements/).
* Tables can't be dragged and dropped into a design.
* Apps can't set the borders of tables.
* A single table can't have more than 225 cells.

## API reference

* [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/)
* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
