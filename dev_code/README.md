# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game. 
The core goal of project is to build trivia API full stack application to be used by Udacity employees and Students.

The application:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Skills Acquired
Completing this trivia  API gives the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Main Files: Project Structure

![folder-hierarchy](https://i.ibb.co/7K1r6Nc/folder-hierarchy.jpg)

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. `flaskr/__init__.py` define endpoints and can reference models.py and config.py for DB and SQLAlchemy setup. `test_flaskr.py` created and designed using `Test-Driven-Development` method for `Unit Tests` to check expected behaviour for successful and for bad requests for each API endpoint.

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. Update the endpoints after defining them in the backend.

## Implementation and Development Tasks

1) [Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 
2) Configure local database and connect it to a web application (Provided by Udacity).
3) Running the flask server
4) Completing backend tasks (
	 - [`./frontend/`](./frontend/README.md)
	 - [`./backend/`](./backend/README.md))
5) Creating unittest (test-driven-development (TDD) for automated testing of APIs 
6) Use "curl" to get responses from API
7) Implement errorhandler to create error messages for trivia API clients
8) Update README.md to document project setup & API endpoints

## Setup Project locally

Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)
