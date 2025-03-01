# API Endpoint Validation and Testing Report with cURL

## 1. Validation Implementation

**User Model**:

- first_name: Must be a non-empty string, max 50 characters.
- last_name: Must be a non-empty string, max 50 characters.
- email: Must be a non-empty, valid email format, and unique.
- password: Must be a string of at least 8 characters.
- is_admin: Must be a boolean.

**Place Model**: 

- name: Must be a non-empty string.
- description: Must be a string.
- city: Must be a string.
- owner_id: Must be a valid User ID.
- latitude: Must be a float between -90 and 90.
- longitude: Must be a float between -180 and 180.
- price: Must be a non-negative float.

**Review Model**:

- text: Must be a non-empty string.
- rating: Must be an integer between 1 and 5.
- user_id: Must reference a valid User.
- place_id: Must reference a valid Place.

## 2. Test Scenarios (using cURL)

**User Endpoint Tests**

Create a valid user:
```bash
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securePass123"
}'
```
*Expected Response*: 200 OK
```bash
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}
```
Create an invalid user (missing fields):
```bash
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "",
    "last_name": "",
    "email": "invalid-email"
}'
```
*Expected Response*: 400 Bad Request
```bash
{
    "error": "Invalid input data"
}
```

***

**Place Endpoint Tests**


