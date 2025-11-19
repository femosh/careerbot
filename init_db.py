"""
Script to initialize the database with sample employee data
"""
from datetime import date
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import crud

# Sample employee data
SAMPLE_EMPLOYEES = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@careerbot.com",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 120000.0,
        "hire_date": date(2020, 1, 15)
    },
    {
        "name": "Bob Smith",
        "email": "bob.smith@careerbot.com",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 95000.0,
        "hire_date": date(2021, 3, 10)
    },
    {
        "name": "Carol Martinez",
        "email": "carol.martinez@careerbot.com",
        "department": "Sales",
        "position": "Sales Manager",
        "salary": 110000.0,
        "hire_date": date(2019, 6, 20)
    },
    {
        "name": "David Lee",
        "email": "david.lee@careerbot.com",
        "department": "Sales",
        "position": "Sales Representative",
        "salary": 75000.0,
        "hire_date": date(2022, 2, 1)
    },
    {
        "name": "Emma Wilson",
        "email": "emma.wilson@careerbot.com",
        "department": "Marketing",
        "position": "Marketing Director",
        "salary": 130000.0,
        "hire_date": date(2018, 9, 5)
    },
    {
        "name": "Frank Brown",
        "email": "frank.brown@careerbot.com",
        "department": "Marketing",
        "position": "Marketing Specialist",
        "salary": 68000.0,
        "hire_date": date(2021, 7, 12)
    },
    {
        "name": "Grace Davis",
        "email": "grace.davis@careerbot.com",
        "department": "HR",
        "position": "HR Manager",
        "salary": 105000.0,
        "hire_date": date(2019, 11, 3)
    },
    {
        "name": "Henry Taylor",
        "email": "henry.taylor@careerbot.com",
        "department": "Finance",
        "position": "Financial Analyst",
        "salary": 90000.0,
        "hire_date": date(2020, 8, 25)
    },
    {
        "name": "Iris Chen",
        "email": "iris.chen@careerbot.com",
        "department": "Engineering",
        "position": "DevOps Engineer",
        "salary": 115000.0,
        "hire_date": date(2021, 1, 18)
    },
    {
        "name": "Jack Anderson",
        "email": "jack.anderson@careerbot.com",
        "department": "Finance",
        "position": "Senior Accountant",
        "salary": 98000.0,
        "hire_date": date(2019, 4, 7)
    }
]


def init_database():
    """Initialize database with sample data"""
    # Create tables
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Check if database is already populated
        existing_employees = db.query(models.Employee).count()
        if existing_employees > 0:
            print(f"Database already contains {existing_employees} employees.")
            response = input("Do you want to clear and repopulate? (yes/no): ")
            if response.lower() != 'yes':
                print("Skipping database initialization.")
                return

            # Clear existing data
            db.query(models.Employee).delete()
            db.commit()
            print("Cleared existing employee data.")

        # Add sample employees
        for emp_data in SAMPLE_EMPLOYEES:
            employee = schemas.EmployeeCreate(**emp_data)
            crud.create_employee(db, employee)

        print(f"Successfully added {len(SAMPLE_EMPLOYEES)} employees to the database!")

        # Display summary
        print("\nDatabase Summary:")
        departments = db.query(models.Employee.department).distinct().all()
        for (dept,) in departments:
            count = db.query(models.Employee).filter(models.Employee.department == dept).count()
            print(f"  {dept}: {count} employees")

    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Initializing CareerBot Employee Database...")
    init_database()
    print("\nDatabase initialization complete!")
