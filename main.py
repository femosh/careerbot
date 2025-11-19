from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import crud
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerBot Employee Management API",
    description="A simple CRUD API for managing employee data",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to CareerBot Employee Management API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "employees": "/employees",
            "create_employee": "/employees (POST)",
            "get_employee": "/employees/{id}",
            "update_employee": "/employees/{id} (PUT)",
            "delete_employee": "/employees/{id} (DELETE)",
            "by_department": "/employees/department/{department}"
        }
    }


@app.post("/employees", response_model=schemas.Employee, status_code=201)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee"""
    return crud.create_employee(db=db, employee=employee)


@app.get("/employees", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all employees with optional pagination"""
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID"""
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.get("/employees/department/{department}", response_model=List[schemas.Employee])
def read_employees_by_department(department: str, db: Session = Depends(get_db)):
    """Get all employees in a specific department"""
    employees = crud.get_employees_by_department(db, department=department)
    return employees


@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing employee"""
    db_employee = crud.update_employee(db, employee_id=employee_id, employee_update=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete an employee"""
    success = crud.delete_employee(db, employee_id=employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Employee {employee_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
