"""
Script to generate API documentation artifact for frontend developers
This creates a JSON file with all endpoint information and example requests/responses
"""
import json
from datetime import datetime


API_DOCUMENTATION = {
    "api_info": {
        "title": "CareerBot Employee Management API",
        "version": "1.0.0",
        "base_url": "http://localhost:8000",
        "description": "A simple CRUD API for managing employee data",
        "generated_at": datetime.now().isoformat()
    },
    "endpoints": [
        {
            "path": "/",
            "method": "GET",
            "description": "Root endpoint with API information",
            "parameters": [],
            "response_example": {
                "message": "Welcome to CareerBot Employee Management API",
                "version": "1.0.0"
            }
        },
        {
            "path": "/employees",
            "method": "GET",
            "description": "Get all employees with optional pagination",
            "parameters": [
                {"name": "skip", "type": "integer", "default": 0, "description": "Number of records to skip"},
                {"name": "limit", "type": "integer", "default": 100, "description": "Maximum number of records to return"}
            ],
            "response_example": [
                {
                    "id": 1,
                    "name": "Alice Johnson",
                    "email": "alice.johnson@careerbot.com",
                    "department": "Engineering",
                    "position": "Senior Software Engineer",
                    "salary": 120000.0,
                    "hire_date": "2020-01-15"
                }
            ],
            "curl_example": "curl -X GET 'http://localhost:8000/employees?skip=0&limit=10'"
        },
        {
            "path": "/employees/{employee_id}",
            "method": "GET",
            "description": "Get a specific employee by ID",
            "parameters": [
                {"name": "employee_id", "type": "integer", "required": True, "description": "Employee ID"}
            ],
            "response_example": {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice.johnson@careerbot.com",
                "department": "Engineering",
                "position": "Senior Software Engineer",
                "salary": 120000.0,
                "hire_date": "2020-01-15"
            },
            "curl_example": "curl -X GET 'http://localhost:8000/employees/1'"
        },
        {
            "path": "/employees/department/{department}",
            "method": "GET",
            "description": "Get all employees in a specific department",
            "parameters": [
                {"name": "department", "type": "string", "required": True, "description": "Department name"}
            ],
            "response_example": [
                {
                    "id": 1,
                    "name": "Alice Johnson",
                    "email": "alice.johnson@careerbot.com",
                    "department": "Engineering",
                    "position": "Senior Software Engineer",
                    "salary": 120000.0,
                    "hire_date": "2020-01-15"
                }
            ],
            "curl_example": "curl -X GET 'http://localhost:8000/employees/department/Engineering'"
        },
        {
            "path": "/employees",
            "method": "POST",
            "description": "Create a new employee",
            "parameters": [],
            "request_body": {
                "name": "John Doe",
                "email": "john.doe@careerbot.com",
                "department": "Engineering",
                "position": "Software Engineer",
                "salary": 100000.0,
                "hire_date": "2023-01-01"
            },
            "response_example": {
                "id": 11,
                "name": "John Doe",
                "email": "john.doe@careerbot.com",
                "department": "Engineering",
                "position": "Software Engineer",
                "salary": 100000.0,
                "hire_date": "2023-01-01"
            },
            "curl_example": """curl -X POST 'http://localhost:8000/employees' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "name": "John Doe",
    "email": "john.doe@careerbot.com",
    "department": "Engineering",
    "position": "Software Engineer",
    "salary": 100000.0,
    "hire_date": "2023-01-01"
  }'"""
        },
        {
            "path": "/employees/{employee_id}",
            "method": "PUT",
            "description": "Update an existing employee",
            "parameters": [
                {"name": "employee_id", "type": "integer", "required": True, "description": "Employee ID"}
            ],
            "request_body": {
                "salary": 125000.0,
                "position": "Lead Software Engineer"
            },
            "response_example": {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice.johnson@careerbot.com",
                "department": "Engineering",
                "position": "Lead Software Engineer",
                "salary": 125000.0,
                "hire_date": "2020-01-15"
            },
            "curl_example": """curl -X PUT 'http://localhost:8000/employees/1' \\
  -H 'Content-Type: application/json' \\
  -d '{
    "salary": 125000.0,
    "position": "Lead Software Engineer"
  }'"""
        },
        {
            "path": "/employees/{employee_id}",
            "method": "DELETE",
            "description": "Delete an employee",
            "parameters": [
                {"name": "employee_id", "type": "integer", "required": True, "description": "Employee ID"}
            ],
            "response_example": {
                "message": "Employee 1 deleted successfully"
            },
            "curl_example": "curl -X DELETE 'http://localhost:8000/employees/1'"
        }
    ],
    "schemas": {
        "Employee": {
            "id": "integer (auto-generated)",
            "name": "string (required)",
            "email": "string (required, unique, valid email)",
            "department": "string (required)",
            "position": "string (required)",
            "salary": "float (required)",
            "hire_date": "date (required, format: YYYY-MM-DD)"
        },
        "EmployeeCreate": {
            "name": "string (required)",
            "email": "string (required, unique, valid email)",
            "department": "string (required)",
            "position": "string (required)",
            "salary": "float (required)",
            "hire_date": "date (required, format: YYYY-MM-DD)"
        },
        "EmployeeUpdate": {
            "name": "string (optional)",
            "email": "string (optional, unique, valid email)",
            "department": "string (optional)",
            "position": "string (optional)",
            "salary": "float (optional)",
            "hire_date": "date (optional, format: YYYY-MM-DD)"
        }
    },
    "common_responses": {
        "200": "Success",
        "201": "Created",
        "404": "Not Found - Resource does not exist",
        "422": "Validation Error - Invalid request data"
    }
}


def generate_markdown():
    """Generate a Markdown version of the API documentation"""
    md_content = f"""# {API_DOCUMENTATION['api_info']['title']}

**Version:** {API_DOCUMENTATION['api_info']['version']}
**Base URL:** {API_DOCUMENTATION['api_info']['base_url']}
**Generated:** {API_DOCUMENTATION['api_info']['generated_at']}

## Description
{API_DOCUMENTATION['api_info']['description']}

## Interactive Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

"""
    for endpoint in API_DOCUMENTATION['endpoints']:
        md_content += f"### {endpoint['method']} {endpoint['path']}\n\n"
        md_content += f"{endpoint['description']}\n\n"

        if endpoint.get('parameters'):
            md_content += "**Parameters:**\n"
            for param in endpoint['parameters']:
                required = " (required)" if param.get('required') else ""
                md_content += f"- `{param['name']}` ({param['type']}){required}: {param['description']}\n"
            md_content += "\n"

        if endpoint.get('request_body'):
            md_content += "**Request Body:**\n```json\n"
            md_content += json.dumps(endpoint['request_body'], indent=2)
            md_content += "\n```\n\n"

        md_content += "**Example Response:**\n```json\n"
        md_content += json.dumps(endpoint['response_example'], indent=2)
        md_content += "\n```\n\n"

        if endpoint.get('curl_example'):
            md_content += "**cURL Example:**\n```bash\n"
            md_content += endpoint['curl_example']
            md_content += "\n```\n\n"

        md_content += "---\n\n"

    md_content += "## Data Schemas\n\n"
    for schema_name, schema_fields in API_DOCUMENTATION['schemas'].items():
        md_content += f"### {schema_name}\n\n"
        for field, field_type in schema_fields.items():
            md_content += f"- **{field}**: {field_type}\n"
        md_content += "\n"

    return md_content


def main():
    """Generate API documentation artifacts"""
    print("Generating API documentation artifacts...")

    # Generate JSON artifact
    json_file = "api_endpoints.json"
    with open(json_file, 'w') as f:
        json.dump(API_DOCUMENTATION, f, indent=2)
    print(f"✓ Generated {json_file}")

    # Generate Markdown documentation
    md_file = "API_DOCUMENTATION.md"
    with open(md_file, 'w') as f:
        f.write(generate_markdown())
    print(f"✓ Generated {md_file}")

    print("\nArtifacts generated successfully!")
    print("\nFrontend developers can use:")
    print(f"  - {json_file} - Structured endpoint data")
    print(f"  - {md_file} - Human-readable documentation")
    print("  - http://localhost:8000/docs - Interactive Swagger UI (when API is running)")
    print("  - http://localhost:8000/openapi.json - OpenAPI specification (when API is running)")


if __name__ == "__main__":
    main()
