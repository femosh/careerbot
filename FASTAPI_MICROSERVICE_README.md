# CareerBot Employee Management Microservice

A simple and complete microservice application with FastAPI backend, SQLite database, and Plotly Dash frontend.

## Project Structure

```
careerbot/
├── database.py              # Database configuration
├── models.py                # SQLAlchemy models
├── schemas.py               # Pydantic schemas for validation
├── crud.py                  # CRUD operations
├── main.py                  # FastAPI application
├── init_db.py              # Database initialization script
├── dashboard.py            # Plotly Dash frontend
├── generate_api_docs.py    # API documentation generator
├── generate_docs.sh        # Batch script for documentation
├── requirements.txt        # Python dependencies
└── careerbot.db           # SQLite database (created after init)
```

## Features

### Backend (FastAPI)
- ✅ RESTful CRUD API for employee management
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Automatic API documentation (Swagger UI)
- ✅ Data validation with Pydantic
- ✅ CORS enabled for frontend integration

### Frontend (Plotly Dash)
- ✅ Interactive dashboard with real-time data
- ✅ Summary statistics (total employees, departments, salaries)
- ✅ Department distribution chart (pie chart)
- ✅ Average salary by department (bar chart)
- ✅ Searchable and sortable employee table
- ✅ Responsive design

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/employees` | Get all employees (with pagination) |
| GET | `/employees/{id}` | Get employee by ID |
| GET | `/employees/department/{dept}` | Get employees by department |
| POST | `/employees` | Create new employee |
| PUT | `/employees/{id}` | Update employee |
| DELETE | `/employees/{id}` | Delete employee |

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize Database

```bash
python3 init_db.py
```

This will create the SQLite database and populate it with 10 sample employees across different departments.

### 3. Generate API Documentation Artifacts

```bash
./generate_docs.sh
# or
python3 generate_api_docs.py
```

This creates two files for frontend developers:
- `api_endpoints.json` - Structured endpoint data
- `API_DOCUMENTATION.md` - Human-readable documentation

## Running the Application

### Start the FastAPI Backend

```bash
# Option 1: Using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using Python
python3 main.py
```

The API will be available at:
- **Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Start the Plotly Dash Frontend

In a new terminal:

```bash
python3 dashboard.py
```

The dashboard will be available at:
- **Dashboard URL**: http://localhost:8050

## Usage Examples

### Using the API (cURL)

#### Get all employees
```bash
curl -X GET 'http://localhost:8000/employees'
```

#### Get employee by ID
```bash
curl -X GET 'http://localhost:8000/employees/1'
```

#### Get employees by department
```bash
curl -X GET 'http://localhost:8000/employees/department/Engineering'
```

#### Create new employee
```bash
curl -X POST 'http://localhost:8000/employees' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Jane Doe",
    "email": "jane.doe@careerbot.com",
    "department": "Engineering",
    "position": "Senior Developer",
    "salary": 130000.0,
    "hire_date": "2023-06-01"
  }'
```

#### Update employee
```bash
curl -X PUT 'http://localhost:8000/employees/1' \
  -H 'Content-Type: application/json' \
  -d '{
    "salary": 135000.0,
    "position": "Principal Engineer"
  }'
```

#### Delete employee
```bash
curl -X DELETE 'http://localhost:8000/employees/1'
```

### Using the API (Python)

```python
import requests

API_URL = "http://localhost:8000"

# Get all employees
response = requests.get(f"{API_URL}/employees")
employees = response.json()
print(employees)

# Create new employee
new_employee = {
    "name": "John Smith",
    "email": "john.smith@careerbot.com",
    "department": "Sales",
    "position": "Account Executive",
    "salary": 85000.0,
    "hire_date": "2023-07-15"
}
response = requests.post(f"{API_URL}/employees", json=new_employee)
created = response.json()
print(f"Created employee with ID: {created['id']}")

# Update employee
update_data = {"salary": 90000.0}
response = requests.put(f"{API_URL}/employees/{created['id']}", json=update_data)
print(response.json())

# Delete employee
response = requests.delete(f"{API_URL}/employees/{created['id']}")
print(response.json())
```

## Database Schema

### Employee Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto-increment |
| name | String | Required |
| email | String | Required, Unique |
| department | String | Required |
| position | String | Required |
| salary | Float | Required |
| hire_date | Date | Required |

## Sample Data

The database is initialized with 10 employees across 5 departments:
- **Engineering**: 3 employees
- **Sales**: 2 employees
- **Marketing**: 2 employees
- **HR**: 1 employee
- **Finance**: 2 employees

## Development

### Adding New Endpoints

1. Add CRUD function in `crud.py`
2. Create route in `main.py`
3. Update documentation in `generate_api_docs.py`
4. Regenerate docs: `./generate_docs.sh`

### Modifying the Database Schema

1. Update model in `models.py`
2. Update schemas in `schemas.py`
3. Delete `careerbot.db`
4. Run `python3 init_db.py` to recreate

### Customizing the Dashboard

Edit `dashboard.py` to add new charts or modify the layout.

## Testing

### Test API Endpoints

```bash
# Install httpie for easier testing
pip install httpie

# Test endpoints
http GET localhost:8000/employees
http GET localhost:8000/employees/1
http POST localhost:8000/employees name="Test User" email="test@example.com" \
  department="Engineering" position="Tester" salary:=75000 hire_date="2023-01-01"
```

### Verify Database

```bash
# Install sqlite3 if not available
sqlite3 careerbot.db "SELECT * FROM employees;"
```

## Troubleshooting

### Port Already in Use
- Backend: Change port in `main.py` (line: `uvicorn.run(app, host="0.0.0.0", port=8000)`)
- Frontend: Change port in `dashboard.py` (line: `app.run_server(debug=True, host='0.0.0.0', port=8050)`)

### Database Errors
- Delete `careerbot.db` and run `python3 init_db.py` again

### CORS Issues
- CORS is enabled for all origins in `main.py`. Modify `allow_origins` for production.

### Dashboard Not Loading Data
- Ensure FastAPI backend is running on http://localhost:8000
- Check browser console for errors
- Verify API is accessible: `curl http://localhost:8000/employees`

## Production Deployment

For production deployment:

1. **Security**:
   - Add authentication/authorization
   - Restrict CORS origins
   - Use environment variables for configuration
   - Enable HTTPS

2. **Database**:
   - Consider PostgreSQL or MySQL instead of SQLite
   - Set up database migrations with Alembic

3. **Deployment**:
   - Use Gunicorn or uWSGI for production ASGI server
   - Deploy behind a reverse proxy (Nginx, Traefik)
   - Use Docker for containerization

## License

This is a sample project for demonstration purposes.

## Author

Generated for CareerBot project.
