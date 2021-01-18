# company-employee
A Python Django REST API based company-employee relationship  
Basically, a employee can have many companies and a company can have many employees  

# Steps to run

- `git clone https://github.com/TeijiW/company-employee.git`
- `pip install -r requirements-dev.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

Since you has been created a super user, you is able to use the API

# Routes

## Token

- **POST** - `/api/api-token-auth/` 
  - Make request with body `{"username": "", "password": ""}`

## Company (/api)
- **GET**
  - LIST - `/company`
  - GET SINGLE - `/company/<company_id>`
- **POST**
  - CREATE - `/company/`
- **PUT**
  - UPDATE - `/company/<company_id>/`
  - ASSIGN EMPLOYEE - `/company/<company_id>/employee/<employee_id>/`
- **DELETE**
  - REMOVE - `/company/<company_id>`
  - REMOVE EMPLOYEE - `/company/<company_id>/employee/<employee_id>/`


## Employee (/api)
- **GET**
  - LIST - `/employee`
  - GET SINGLE - `/employee/<employee_id>`
- **POST**
  - CREATE - `/employee/`
- **PUT**
  - UPDATE - `/employee/<employee_id>/`
  - ASSIGN EMPLOYEE - `/employee/<employee_id>/company/<company_id>/`
- **DELETE**
  - REMOVE - `/employee/<employee_id>`
  - REMOVE EMPLOYEE - `/employee/<employee_id>/company/<company_id>/`


# Models

## Employee

- `email`
  - Unique
  - Required
- `name`
  - Max length: 256
  - Required
- `username`
  - Max length: 256
  - Unique
  - Required

## Company

- `city`
  - Max length: 128
- `country`
  - Max length: 128
- `name`
  - Max length: 256
  - Unique
  - Required
