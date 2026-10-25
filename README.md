# Command-Line API Explorer

## Project Purpose

A Python command-line application that retrieves posts and todos from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API.

## Requirements

- Python 3
- `requests` library

## Setup

Install the required library:

```bash
py -m pip install requests
```

## Run the Application

Open a terminal in the project directory and run:

```bash
py l1json.py
```

## Available Operations

1. Fetch a post by its ID.
2. Fetch todos by user ID.
3. Exit the application.

The application displays post details or the todo ID, title, and completion status.

## Error Handling

The application handles:

- Connection and network errors.
- HTTP errors, including unsuccessful status codes.
- Invalid JSON responses.
- Invalid menu choices and IDs.
- Empty todo results, which are reported as no todos found.

The menu remains available after handled request failures.

## Run the Tests

Execute the test script:

```bash
py test.py
```

The tests use mocked HTTP responses to verify successful post and todo retrieval, simulated connection failures, invalid JSON, and HTTP errors without relying on real network failures.

Import safety can be checked separately with:

```bash
py -c "import l1json; print('Import completed successfully')"
```

Importing the application module should not launch the interactive menu.
