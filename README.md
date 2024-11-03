# Enviroplus-QL

Enviroplus-QL is a GraphQL server designed for querying sensor data from the Enviroplus Raspberry Pi HAT made by Pimoroni. This project leverages FastAPI and Strawberry GraphQL to provide a high-performance, easy-to-use API for accessing environmental sensor data.

## How it Works
A GraphQL server allows clients to request exactly the data they need, making it more efficient than traditional REST APIs, which is exactly why it was chosen for the newest version of our Enviroplus Web Dashboard application.

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python based on standard Python type hints. It bolsters the efficiency of our GraphQL server implementation in a number of ways:

- Asynchronous Capability: FastAPI supports asynchronous programming, allowing the server to handle many requests concurrently without blocking. This is particularly useful for I/O-bound operations like database queries.
- Automatic Validation: FastAPI automatically validates request data against the defined types, reducing the need for manual validation and improving reliability.
- High Performance: Built on top of Starlette for the web parts and Pydantic for the data parts, FastAPI is designed to be one of the fastest Python frameworks available.
- Ease of Use: FastAPI's use of Python type hints makes it easy to write and maintain code, while also providing excellent editor support and auto-completion.

<br>

**By combining GraphQL with FastAPI, you get a powerful, efficient, and easy-to-use server for querying sensor data from the Enviroplus Raspberry Pi HAT.**

## Installation

**Clone the repository:**
```sh
git clone https://github.com/yourusernameenviroplus-ql.git
cd enviroplus-ql
```

**Install dependencies using Poetry:**
```sh
poetry install
```

### Running the Server

**To start the server, use the following command:**
```sh
poetry run enviroplus-ql
```
