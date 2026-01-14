\# Task Manager API



This project is a simple RESTful API built using FastAPI as part of a backend fundamentals assignment.

The goal of the project is to demonstrate understanding of REST APIs, clean code structure,

and version control using GitHub.



The API allows clients to create, retrieve, update, and delete tasks using HTTP requests.

There is no graphical user interface; the project focuses on backend logic only.



---



\## Project Overview



The Task Manager API provides basic task management functionality.

Each task contains an ID and a title, and the API exposes endpoints to manage these tasks.



The project is designed to be simple and extendable so it can later be integrated

with frontend applications or AI-based systems.



---

\## Project Structure

app/

 ├── main.py

 ├── routes/

 ├── models/

 └── services/

--

\## Technologies Used



\- Python

\- FastAPI

\- Uvicorn

\- Git \& GitHub

\- Virtual Environment (venv)



---



\## How to Download, Install, and Run the Project



1\. Clone the repository from GitHub

2\. Create and activate a virtual environment

3\. Install project dependencies

4\. Run the FastAPI server

5\. Open your browser and access the API documentation:http://127.0.0.1:8000/docs



----------------------

This page allows you to test all API endpoints directly.



---



\## API Endpoints



\- GET /tasks  

&nbsp; Retrieves all tasks.



\- POST /tasks  

&nbsp; Creates a new task.



\- PUT /tasks/{id}  

&nbsp; Updates an existing task.



\- DELETE /tasks/{id}  

&nbsp; Deletes a task.



All requests and responses use JSON format.



---



\## Clean Code Practices



The project follows clean code principles by:

\- Using clear and meaningful naming

\- Separating application logic into organized files

\- Keeping functions small and readable

\- Handling errors in a simple and clear way



---



\## Docker



Docker support was planned for this project.

A Dockerfile is included to demonstrate containerization setup.

Due to environment-related limitations, the container was not run locally,

but the project is ready to be containerized on any supported system.

Docker Note
Due to local environment limitations, Docker was tested successfully using an online Docker playground.
Screenshots of build and run steps are attached as proof of execution.

---



\## Author



Abrar  

Unified Developer Foundation Project



