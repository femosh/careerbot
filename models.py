from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class Employee(Base):
    """Employee model for SQLite database"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    department = Column(String)
    position = Column(String)
    salary = Column(Float)
    hire_date = Column(Date)

    def __repr__(self):
        return f"<Employee(name={self.name}, department={self.department})>"
