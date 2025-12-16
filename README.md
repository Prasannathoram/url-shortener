# URL SHORTENER SERVICE WITH ANALYTICS

# 



### OVERVIEW

---------------

This project is a backend URL shortening service similar to bit.ly or t.co.

It converts long URLs into short, manageable aliases, handles HTTP redirects

efficiently, and tracks usage analytics such as click counts.



The project demonstrates core backend development concepts including REST API

design, database schema modeling, unique constraints, indexing, and analytics

tracking.





### 

### TECH STACK

-------------------

Programming Language : Python

Web Framework        : FastAPI

Database             : SQLite

ORM                  : SQLAlchemy

API Documentation    : Swagger / OpenAPI





### 

### FEATURES

---------------

• Generate short URLs for long original URLs

• Redirect short URLs using HTTP 302 status code

• Track click analytics for each short URL

• Provide usage statistics

• Proper error handling for invalid or non-existent short codes





### 

### PROJECT STRUCTURE

--------------------------------

url-shortener/

│

├── app/

│   ├── main.py        → FastAPI application \& API routes

│   ├── database.py    → Database configuration

│   ├── models.py      → Database models

│   ├── schemas.py     → Request \& response schemas

│   ├── utils.py       → Short code generation logic

│   └── urls.db        → SQLite database (auto-generated)

│

├── README.md          → Project documentation

├── .gitignore         → Git ignore rules

└── venv/              → Virtual environment



### 

### SETUP AND RUN INSTRUCTIONS

-------------------------------------------------

## OpenAPI / Swagger Specification

This project includes an OpenAPI (Swagger) specification file that describes all API endpoints, request/response formats, and models.

The specification file is generated automatically by FastAPI and is included in this repository as:

openapi.json

This file can be:
- Viewed directly on GitHub
- Imported into tools such as Postman, Insomnia, or Swagger Editor
- Used by evaluators to easily test all API endpoints

When running the application locally, interactive API documentation is also available at:

http://127.0.0.1:8000/docs

The raw OpenAPI specification can be accessed locally at:

http://127.0.0.1:8000/openapi.json




#### Step 1: Clone the Repository

--------------------------------------------

git clone <github-repo-url>

cd url-shortener





#### Step 2: Create Virtual Environment

------------------------------------------------------

python -m venv venv





#### Step 3: Activate Virtual Environment

---------------------------------------------------------

Git Bash (Windows):

source venv/Scripts/activate



Once activated, (venv) will appear in the terminal.





#### Step 4: Install Dependencies

---------------------------------------------

pip install fastapi uvicorn sqlalchemy pydantic





#### Step 5: Run the Application

-------------------------------------------

cd app

uvicorn main:app --reload



Server will start at:

http://127.0.0.1:8000





#### Step 6: Open Swagger UI

-------------------------------------

http://127.0.0.1:8000/docs



Swagger UI allows interactive testing of all endpoints.





### 

### 

### API DOCUMENTATION

--------------------------------



#### POST /api/shorten

---------------------------

Description:

Creates a shortened URL from a long URL.



Request Body:

{

&nbsp; "original\_url": "https://www.google.com"

}



Response:

{

&nbsp; "short\_code": "000001"

}



cURL Example:

curl -X POST http://127.0.0.1:8000/api/shorten \\

-H "Content-Type: application/json" \\

-d '{"original\_url":"https://www.google.com"}'





#### GET /{short\_code}

---------------------------

Description:

Redirects the client to the original URL.



Example:

http://127.0.0.1:8000/000001



Behavior:

• Redirects to original URL

• Uses HTTP 302 Found

• Records a click for analytics





#### GET /api/stats/{short\_code}

-------------------------------------------

Description:

Returns analytics for a shortened URL.



Response:

{

&nbsp; "short\_code": "000001",

&nbsp; "total\_clicks": 1

}



cURL Example:

curl http://127.0.0.1:8000/api/stats/000001



### 

### 

### ERROR HANDLING

--------------------------

If a non-existent or invalid short code is requested, the API returns:



{

&nbsp; "detail": "Short URL not found"

}



HTTP Status Code: 404 Not Found





### 

### 

### SHORT CODE GENERATION STRATEGY

--------------------------------------------------------

The service uses a Base62 encoding strategy.



• Each URL is first stored in the database

• The database generates a unique auto-incremented ID

• This ID is encoded into a Base62 string

• The encoded value is padded to a fixed length



Base62 uses digits and uppercase/lowercase letters, making the short codes

URL-safe and compact.





### 

### COLLISION HANDLING STRATEGY

---------------------------------------------------

Collisions are prevented by design:



• Auto-incremented primary key ensures uniqueness

• Deterministic Base62 encoding

• UNIQUE constraint on the short\_code column

• Database enforces data integrity





### 

### TESTING

-------------

• Swagger UI (/docs)

• Browser (for redirect testing)

• cURL commands provided above





### 

### CONCLUSION

-------------------

This project implements a complete and reliable URL shortening microservice

with analytics. It follows best practices in backend development, database

design, API documentation, and error handling, making it suitable for

evaluation and real-world use.



