from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas


def get_employee(db: Session, employee_id: int) -> Optional[models.Employee]:
    """Get a single employee by ID"""
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100) -> List[models.Employee]:
    """Get all employees with pagination"""
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employees_by_department(db: Session, department: str) -> List[models.Employee]:
    """Get all employees in a specific department"""
    return db.query(models.Employee).filter(models.Employee.department == department).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate) -> models.Employee:
    """Create a new employee"""
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(
    db: Session, employee_id: int, employee_update: schemas.EmployeeUpdate
) -> Optional[models.Employee]:
    """Update an existing employee"""
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        return None

    update_data = employee_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int) -> bool:
    """Delete an employee"""
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        return False

    db.delete(db_employee)
    db.commit()
    return True
