from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class EmployeeBase(BaseModel):
    """Base schema for Employee"""
    name: str
    email: EmailStr
    department: str
    position: str
    salary: float
    hire_date: date


class EmployeeCreate(EmployeeBase):
    """Schema for creating an Employee"""
    pass


class EmployeeUpdate(BaseModel):
    """Schema for updating an Employee"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    hire_date: Optional[date] = None


class Employee(EmployeeBase):
    """Schema for Employee response"""
    id: int

    class Config:
        from_attributes = True
