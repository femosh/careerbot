# CareerBot Employee Management API

**Version:** 1.0.0
**Base URL:** http://localhost:8000
**Generated:** 2025-11-19T19:05:51.857866

## Description
A simple CRUD API for managing employee data

## Interactive Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### GET /

Root endpoint with API information

**Example Response:**
```json
{
  "message": "Welcome to CareerBot Employee Management API",
  "version": "1.0.0"
}
```

---

### GET /employees

Get all employees with optional pagination

**Parameters:**
- `skip` (integer): Number of records to skip
- `limit` (integer): Maximum number of records to return

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice.johnson@careerbot.com",
    "department": "Engineering",
    "position": "Senior Software Engineer",
    "salary": 120000.0,
    "hire_date": "2020-01-15"
  }
]
```

**cURL Example:**
```bash
curl -X GET 'http://localhost:8000/employees?skip=0&limit=10'
```

---

### GET /employees/{employee_id}

Get a specific employee by ID

**Parameters:**
- `employee_id` (integer) (required): Employee ID

**Example Response:**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@careerbot.com",
  "department": "Engineering",
  "position": "Senior Software Engineer",
  "salary": 120000.0,
  "hire_date": "2020-01-15"
}
```

**cURL Example:**
```bash
curl -X GET 'http://localhost:8000/employees/1'
```

---

### GET /employees/department/{department}

Get all employees in a specific department

**Parameters:**
- `department` (string) (required): Department name

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice.johnson@careerbot.com",
    "department": "Engineering",
    "position": "Senior Software Engineer",
    "salary": 120000.0,
    "hire_date": "2020-01-15"
  }
]
```

**cURL Example:**
```bash
curl -X GET 'http://localhost:8000/employees/department/Engineering'
```

---

### POST /employees

Create a new employee

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@careerbot.com",
  "department": "Engineering",
  "position": "Software Engineer",
  "salary": 100000.0,
  "hire_date": "2023-01-01"
}
```

**Example Response:**
```json
{
  "id": 11,
  "name": "John Doe",
  "email": "john.doe@careerbot.com",
  "department": "Engineering",
  "position": "Software Engineer",
  "salary": 100000.0,
  "hire_date": "2023-01-01"
}
```

**cURL Example:**
```bash
curl -X POST 'http://localhost:8000/employees' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe",
    "email": "john.doe@careerbot.com",
    "department": "Engineering",
    "position": "Software Engineer",
    "salary": 100000.0,
    "hire_date": "2023-01-01"
  }'
```

---

### PUT /employees/{employee_id}

Update an existing employee

**Parameters:**
- `employee_id` (integer) (required): Employee ID

**Request Body:**
```json
{
  "salary": 125000.0,
  "position": "Lead Software Engineer"
}
```

**Example Response:**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@careerbot.com",
  "department": "Engineering",
  "position": "Lead Software Engineer",
  "salary": 125000.0,
  "hire_date": "2020-01-15"
}
```

**cURL Example:**
```bash
curl -X PUT 'http://localhost:8000/employees/1' \
  -H 'Content-Type: application/json' \
  -d '{
    "salary": 125000.0,
    "position": "Lead Software Engineer"
  }'
```

---

### DELETE /employees/{employee_id}

Delete an employee

**Parameters:**
- `employee_id` (integer) (required): Employee ID

**Example Response:**
```json
{
  "message": "Employee 1 deleted successfully"
}
```

**cURL Example:**
```bash
curl -X DELETE 'http://localhost:8000/employees/1'
```

---

## Data Schemas

### Employee

- **id**: integer (auto-generated)
- **name**: string (required)
- **email**: string (required, unique, valid email)
- **department**: string (required)
- **position**: string (required)
- **salary**: float (required)
- **hire_date**: date (required, format: YYYY-MM-DD)

### EmployeeCreate

- **name**: string (required)
- **email**: string (required, unique, valid email)
- **department**: string (required)
- **position**: string (required)
- **salary**: float (required)
- **hire_date**: date (required, format: YYYY-MM-DD)

### EmployeeUpdate

- **name**: string (optional)
- **email**: string (optional, unique, valid email)
- **department**: string (optional)
- **position**: string (optional)
- **salary**: float (optional)
- **hire_date**: date (optional, format: YYYY-MM-DD)

