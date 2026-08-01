Source: https://www.canva.dev/docs/apps/design-guidelines/data-connector/

# Data Connector

Guidelines for designing Data Connectors.

[Data Connectors](https://www.canva.dev/docs/apps/intents/data-connector/) present unique design challenges. Users need to navigate external data sources, understand what they're importing, and handle potential errors — all within the constraints of Canva's interface.

These guidelines address the specific design problems you'll encounter when building Data Connectors.

## Designing a Data Connector

### Deliver relevant, real-world data to users

Think about real-world applications like sales reports, marketing dashboards, or research summaries to inform your design. Empower users to make meaningful use of the imported data.

### Keep it simple

Data might seem complex, but sharing it should be straightforward, aligning with our Canva Design Principles. Use the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) for a clear, robust interface. Gradually introduce advanced options with progressive disclosure, ensuring users feel comfortable and in control.

### Access data easily

Consider the user journey from opening the Data Connector to having the data live in Canva. Just like our [Authentication guidelines](https://www.canva.dev/docs/apps/design-guidelines/authentication/), keep login user-friendly. Always provide Search and Filter options to help users find and explore data easily.

### Always offer a way forward

Occasionally, data might not be available. When it's due to known issues such as a search keyword issue or error, inform the user and offer alternatives such as related data or keywords. Encourage them to recover the data themselves for a positive experience.

## Functional expectations

### Prioritize data integrity and reliability

Your Data Connector acts as a trusted pipeline for user data. Validate all imported data rigorously and handle edge cases gracefully. When things go wrong, provide helpful error messages that guide users toward solutions. Implement retry mechanisms for network failures and ensure your app behaves predictably even when data sources become temporarily unavailable.

### Optimize for performance at every step

Nobody likes waiting for data to load. Implement pagination and efficient transformation techniques to keep your app responsive even with large datasets. Be smart about when to fetch data—only retrieve what's needed when it's needed. Consider caching strategies for frequently accessed sources to minimize repeated external requests.

### Security and privacy

Users trust you with their data. Handle that responsibility with care. Follow the principle of least privilege when requesting scopes, implement proper authentication flows, and never store credentials directly in your app. Be transparent about what data is being accessed and how it will be used.

## Design patterns

### Search and filter

* Search fields must be prominently positioned and easy to access
* Filters must support search
* Consider grouping similar filters to avoid excess scrolling
* Use a consistent filter interaction pattern (e.g., checkbox list with search), and omit filters that yield no results

Whenever possible, there must be fallback states when searches return no data. Consider displaying suggested results if applicable.

### Query results and detail views

* Use list views to return search results with clarity and consistency
* Support quick scannability. Consider deferring complex breakdowns or visualizations to a secondary view
* If additional insights or breakdowns are available, consider using progressive disclosure to reveal them when relevant

### Authentication and login

* If your app uses public data, you must allow access without requiring login
* Login prompts must be delayed until the user tries to access protected data or perform actions
* You must provide a clear visual difference between logged-in and logged-out states

### App structure and task flows

* If your connector supports multiple functions (e.g., fetching, cleaning, visualizing), consider using an initial screen to route users
* Split long or complex tasks into smaller, guided steps

### Premium features

* Let free users interact with free features and preview premium ones
* If the app includes premium features, distinguish them with clear labels and familiar icons

## Error handling

### User-friendly errors

Translate technical errors into actionable messages that users can understand. Categorize errors by type and provide specific recovery suggestions for common issues. While keeping user-facing messages simple, log detailed information to help with troubleshooting.

### Graceful degradation

Maintain partial functionality when possible rather than failing completely. Consider caching previous results to use as fallback when fresh data can't be retrieved, and implement progressive enhancement to ensure basic functionality even in challenging conditions.

## Metadata usage

### Rich descriptions

Include comprehensive metadata with each dataset, including source attribution, last-updated timestamps, and relevant categorization. This information helps users understand the context and currency of the data they're working with.

### Formatting hints

Provide formatting metadata for numerical values to ensure they display correctly in Canva designs. Specify units of measurement and include localization information when relevant to help with proper data presentation.

## Refresh mechanism

### Data source references

Create compact, efficient references (under 5KB) that contain everything needed for future refreshes. Version your reference format to support evolution over time, and handle expired or invalid references gracefully so users aren't stranded if their data source changes.

## Testing and validation

### Data quality checks

Validate against Canva's size and complexity limits (max 20 columns, 100 rows by default, 200KB total size). Check for malformed or inconsistent data and test thoroughly with edge cases like extremely large or small values.

### Performance testing

Benchmark your Data Connector with realistically sized datasets under varied network conditions. Measure memory usage during transformation operations and optimize critical paths based on profiling results to ensure a smooth user experience.

## Implementation checklist

* [ ] App correctly implements the required Data Connector actions
* [ ] Data selection UI adapts based on context (new selection vs. edit)
* [ ] Error handling covers all common failure scenarios
* [ ] Data validation respects Canva's format and size limits
* [ ] Refresh mechanism reliably retrieves the latest data
* [ ] Performance is optimized for both small and large datasets
* [ ] Security best practices are followed for all external connections
