Source: https://www.canva.dev/docs/connect/api-requests-responses/

# API requests and responses

API requests (submitted to an API endpoint) tell the endpoint to do something. Once the request is processed, the API endpoint sends a response.

To make API requests, you must know the HTTP method, URL path, and parameters for the endpoint that you want to use.

An API request consists of the combination of the following:

`HTTP method + URL path of the endpoint + request parameters`

## HTTP method and URL path

An *HTTP method* is the operation that you want the endpoint to execute. REST [HTTP methods](https://www.restapitutorial.com/lessons/httpmethods.html) can be:
* POST (create)
* GET (read)
* PUT (update/replace)
* PATCH (update/modify)
* DELETE (delete).

The *URL path* is the HTTP URL where the endpoint can be accessed.

## Request parameters

Parameters can be of the following types:
* `required` (the request cannot go through without the parameter)
* `optional` (the parameter value is supplemented with the default value)

We use the following parameters in Canva REST APIs:
* Path parameters
* Query parameters
* Header parameters
* Body parameters

## API responses

API responses indicate whether an API request was successful. A response consists of an HTTP response status code and a response body that includes either a successful response or an error response.

### HTTP response status code

[HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) indicate whether your request was successful. They include the following types:
* Informational response: 100 - 199
* Successful response: 200 - 299
* Redirection message: 300 - 399
* Client error response: 400 - 499
* Server error response: 500 - 599

### Response body

#### Success response

If your API request has completed successfully, you'll receive a success response that includes the required properties, usually in JSON format.

#### Error response

If your API request doesn't complete successfully, you'll get an error response that consists of the following:
* Error HTTP status code
* Error code (usually includes different information to the status code)
* Error message

## Asynchronous job endpoints

Some Connect APIs are asynchronous. This means that the endpoint doesn't return the response immediately. Instead, it creates a job to process the request and returns a job ID that you can use to check the status of the job.

### Asynchronous job API workflow

The typical flow for using an asynchronous job API is as follows:

1. Submit a request to the 'Create [API name] job' API.
2. If the request was valid, the API returns a response that includes a `job` with an `id`, and a `status` of `in_progress`.
3. Use the job ID to poll the 'Get [API name] job' API until the job status changes from `in_progress` to either `success` or `failed`.
4. Use the result of the finished job to do the next steps in your integration.

### Job polling strategies

We recommend that you use an [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) strategy to poll the job status.

## Trial quotas

Trial quotas provide users on free Canva plans with temporary access to certain premium APIs that are normally restricted to paid plans. These trials allow users to evaluate premium functionality before upgrading their subscription.
