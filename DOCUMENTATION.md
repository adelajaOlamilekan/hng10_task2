# Overview

This is a FastAPI built API for performing **CRUD ( Create, Read, Update and Delete)** operations on **Persons** resource. 

You can create new records using the `POST` verb without adding the `user_id` to the URL. 

By providing the `user_id` and specifying the corresponding `HTTP` verbs, you can update, get and delete a record.

Detailed information about each **endpoints** can be found below.

## Table of Contents

- [Getting Started]()
- [Endpoints]()
    - [1. Create a Person]()
    - [2. Get All Persons]()
    - [3. Get a Person by ID]()
    - [4. Update a Person]()
    - [5. Delete a Person]()
- [Request and Response Examples]()
- [Validation]()
- [Limitation of the API]()
- [Contact Information]()
    

## Getting Started

For how to setup the application; check the README file here: https://github.com/adelajaOlamilekan/hng10_task2/blob/main/README.md

## Endpoints

The API provides the following endpoints for managing the persons resource:

### 1\. Create a Person

- **Endpoint**: `POST /api`
- **Description**: This creates a new person.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Request Body**: JSON object with person information, such as `name` .
- **Response**: JSON object of the created person with an auto-generated `id`.
    

### 2\. Get All Persons

- **Endpoint**: `GET /api`
- **Description** : This returns records of all persons.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Response**: JSON array of all persons in the database.
    

### 3\. Get a Person by ID

- **Endpoint**: `GET /api/{user_id}`
- **Description** : This returns the details of a single person.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Response**: JSON object of the person with the specified `id` or customized error message **(404)** if person not found.
    

### 4\. Update a Person

- **Endpoint**: `PUT /api/{user_id}`
- **Description** : This updates/edits the resource
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Request Body**: JSON object with updated person information, such as `name`.
- **Response**: JSON object of the updated person or customized error message **(404)** if person not found.
    

### 5\. Delete a Person

- **Endpoint**: `DELETE /api/{user_id}`
- **Description** : This deletes a resource
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Response**: JSON object of success message confirming the deletion.
    

## Request and Response Examples

Here are some examples of how to use the API:

### 1\. Create a Person

- `POST /api/   Content-Type: application/json`

```javascript
{  
    "name": "Dominic Toretto",
}
```
- Responses: 

>Status code: 200

```javascript
{  
    "id":1,
    "name": "Dominic Toretto"
}
```

### 2\. Get All Persons

- `GET /api/`
- Responses:

>Status code: 200

```javascript
[
    {  
        "id" : 1,
        "name" : "Akorede Lamidi",
    },
    {  
        "id" : 2,
        "name" : "Ifekunle",
    },   // More persons...
] 
```
    

### 3\. Get a Person by ID

- `GET /api/1`
- Responses:

>Status code: 200

```javascript
{  
    "id" : 1,
    "name" : "Akorede Lamidi"
}
```

>Status code: 404

```javascript
{  
    "error" : "Record not found!"
}
```
### 4\. Update a Person

- `PUT /api/1  Content-Type: application/json`      
- Request body:

```javascript
{
    "name" : "Akorede Gabriel"
}
```

>Response: 200

```javascript
{  
    "message" : " Record updated!",
}
```

>Response: 404
    
 ```javascript
{  
    "error" : " Record not found!",
}
```
### 5\. Delete a Person

- `DELETE /api/1`

>Response: 200

```javascript
{
    "message": "Person with ID 1 has been deleted."
}
```

---

## Validation

The API includes basic validation rules for request data. Ensure your requests follow the specified data format and constraints to avoid validation errors. For example in the request body, the name field can only accept a `string` data type.


## Limitations of the API

While the provided Person API serves as a basic CRUD example, it has certain limitations that may need to be addressed depending on your project requirements:

1. **Authentication and Authorization**: The API lacks authentication and authorization mechanisms. It assumes that all users have access to all endpoints. In a real-world scenario, you would need to implement proper authentication and authorization to restrict access based on user roles and permissions.
2. **Validation**: Although the API includes basic validation rules, it may not cover all potential input scenarios. Custom validation rules for specific data constraints may be required.
3. **Error Handling**: While the API provides error messages and HTTP status codes, the error messages may not always provide detailed information for debugging. Enhanced error handling and logging may be needed for production use.

## Contact Information

For inquiry promotion or support, contact RahmanAkorede at rahmanakorede442@gmail.com or +2347012803737
