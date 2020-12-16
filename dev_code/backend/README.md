# Full Stack Trivia API Backend

1.  [Start Project locally](#start-project)
2.  [API Documentation](#api-documentation)

<a name="start-project"></a>
## Start Project locally

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

A virtual environment whenever using Python for projects, keeps dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Initialize and activate a virtualenv:
```bash
  cd YOUR_PROJECT_DIRECTORY_PATH/
  virtualenv
  source env/Scripts/activate
```

#### PIP Dependencies

Install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
createdb trivia
createdb trivia_test
psql trivia < trivia.psql
```
Change database configuration so it can connect to local postgres database
- Open `config.py` with editor. 
- Add the following:
 ```python
 database_setup = {
    "database_name_production" : "trivia",
    "database_name_test" : "trivia_test",
    "user_name" : "postgres", # default postgres user name
    "password" : "password123", # If no password, type in None
    "port" : "localhost:5432" # default postgres port
}
 ```

## Running the server

From within the `backend` directory first ensure working using created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Testing

-  Execute test cases created by `test_flaskr.py`
-  To execute test cases, run
```bash 
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
-  Run all tests, it should give this response if everything went fine:
```bash
$ python test_flaskr.py
C:\Users\Hp\AppData\Local\Programs\Python\Python39\lib\site-packages\sqlalchemy\
util\langhelpers.py:254: SADeprecationWarning: The 'postgres' dialect name has b
een renamed to 'postgresql'
  loader = self.auto_fn(name)
............
----------------------------------------------------------------------
Ran 12 tests in 2.209s

OK
```

## Tasks

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

<a name="api-documentaton"></a>
## API Documentation

API is not hosted on a specific domain, it can only be accessed when
`flask` is run locally. To make requests to the API via `curl`,
you need to use the default domain on which the flask server is running.

**_http://127.0.0.1:5000/_**

### Available Endpoints

1. Questions
   -  [GET /questions](#get-questions)
   -  [POST /questions](#post-questions)
   -  [POST /questions/search](#search-questions)
   -  [DELETE /questions/<question_id>](#delete-questions)
2. Categories
   -  [GET /categories](#get-categories)
   -  [GET /categories/<category_id>/questions](#get-questions-by-category)
3. Quizzes
   -  [POST /quizzes](#post-quizzes)

# <a name="get-questions"></a>
### 1. GET /questions

#### Description
    Fetch all questions with all available fields(answer, category, difficulty),
    a list of all categories and number of total questions.
#### Request Arguments
    page, optional (10 question per page), defaults to `1` if not given
#### Returns
    List of questions (`id`, `question`, `answer`, `category`, `difficulty`)
    all `categories`
    `current_category`
    `total_questions`
    `success`
#### curl Command
```bash
curl -X GET http://127.0.0.1:5000/questions?page=1
```
#### Response Examples
-  If success:
```js
   .... },
    {
      "answer": "The Liver",
      "category": "1",
      "difficulty": 4,
      "id": 8,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```
-  Error if page does not exists:
```bash
curl -X GET http://127.0.0.1:5000/questions?page=1000
```
```js
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```
# <a name="post-questions"></a>
### 2. POST /questions

#### Description
    Create new Question
#### Request Arguments
    `new_question` - required
    `new_answer` - required
    `difficulty` defaulted by 1, can be changed from drop down list
    `category`  defaulted by first catgory in drop down list 
#### Returns
    `created`  id from new question created 
    `questions` all questions 
    `total_questions` 
    `success`
#### curl Command
```bash
curl -X POST http://127.0.0.1:5000/questions -d '{ "question" : 
"What company did the founders of YouTube work for before starting up YouTube?", 
"category" : "5" , "answer" : "PayPal", "difficulty" : 1 }' 
-H 'Content-Type: application/json'
```
#### Response Examples
-  If success:
```js
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports",
    "7": "Technology"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
        {.... },
    {
      "answer": "He Didn't Graduate From College",
      "category": "7",
      "difficulty": 1,
      "id": 20,
      "question": "What year did Bill Gates graduate from Harvard?"
    },
    {
      "answer": "PayPal",
      "category": "5",
      "difficulty": 1,
      "id": 48,
      "question": "What company did the founders of YouTube work for 
        before starting up YouTube?"
    }
  ],
  "success": true,
  "total_questions": 20
}

```
-  If question not created due too no answer added:
```bash
 curl -X POST http://127.0.0.1:5000/questions -d 
 '{ "question" : "What company did the founders of YouTube work for before starting up YouTube?", 
 "category" : "5" , "answer" : "", "difficulty" : 1 }' 
 -H 'Content-Type: application/json'
```
```js
{
  "error": 400,
  "message": "Answer can not be blank",
  "success": false
}
```
# <a name="search-questions"></a>
### 3. GET /questions/search

#### Description
    Search for questions by given search term
#### Request Arguments
    `searchTerm` - required
#### Returns
    List of `questions` which match the `searchTerm` with fields:
        (`id`, `question`, `answer`, `category`, `difficulty`)
    `total_questions`
    `current_category` with fields: (`id`, `type`)
#### curl Command
```bash
curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm" : "Egypt"}' -H 'Content-Type: application/json'
```
#### Response Examples
-  IF success:
```js
{
  "current_category": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    },
    {
      "id": 7,
      "type": "Technology"
    }
  ],
  "questions": [
    {
      "answer": "Scarab",
      "category": "4",
      "difficulty": 4,
      "id": 1,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```
-  If searchTerm not found:
```bash
 curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm" : "apple"}' -H 'Content-Type: application/json'
```
```js
{
  "error": 404,
  "message": "No questions contains found.",
  "success": false
}
```
# <a name="delete-questions"></a>
### 4. DELETE /questions/<question_id>

#### Description
    Delete Question by question ID
#### Request Arguments
    `question_id` - required
#### Returns
#### curl Command
```bash
curl -X DELETE http://127.0.0.1:5000/questions/48
```
#### Response Examples
```js
{
  "deleted:": 48,
  "questions": [
    {
      "answer": "Scarab",
      "category": "4",
      "difficulty": 4,
      "id": 1,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
 ....
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```
-  If question ID wrong or no question ID provided:
```bash
curl -X DELETE http://127.0.0.1:5000/questions
```
```js
{
  "error": 405,
  "message": "method not allowed",
  "success": false
}
```
# <a name="get-categories"></a>
### 5. GET /categories

#### Description
    Fetches a all `categories` with `id` and `type` as values.
#### Request Arguments
    None
#### Returns
    Returns: A list of categories with its `id` and `type` as values
#### curl Command
```bash
curl -X GET http://127.0.0.1:5000/categories
```
#### Response Examples
```js
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports",
    "7": "Technology"
  },
  "success": true
}
```
-  If endpoint route not exists
```bash
curl -X GET http://127.0.0.1:5000/category
```
```js
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```
# <a name="get-questions-by-category"></a>
### 6. GET /categories/\<category_id\>/questions

#### Description
    Get questions based on category ID

#### Request Arguments
    `category_id` - required
    `page` - optinal (10 questions per Page, defaults to `1` )
#### Returns
    `current_category` id from inputted category
      2. List of dict of all questions with following fields:
         - **integer** `id` 
         - **string** `question`
         - **string** `answer`
         - **string** `category`
         - **integer** `difficulty`
      3. **integer** `total_questions`
      4. **boolean** `success`
#### curl Command
```bash
curl -X GET http://127.0.0.1:5000/categories/2/questions?page=1
```
#### Response Examples
```js
{
  "current_category": {
    "2": "Art"
  },
  "questions": [
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of
 optical illusions?Art"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?Art"
    },
    {
      "answer": "One",
      "category": "2",
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?Art"
    }
  ],
  "success": true,
  "total_questions": 3
}
```
-  If no category ID provided:
```bash
 curl -X GET http://127.0.0.1:5000/categories/questions?page=1
```
```js
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```
# <a name="post-quizzes"></a>
### 7. POST /quizzes

#### Description
    Plays quiz game getting list of already asked questions and a category  as an arguments to ask for random question.
#### Request Arguments
    None
#### Returns
    `question` fields(`answer`, `category`, `difficulty`, `id`)
    `success`
#### curl Command
```bash
curl -X POST http://127.0.0.1:5000/quizzes -d '{"previous_questions" : [1, 2, 5], 
"quiz_category" : {"type" : "Science", "id" : "1"}} ' -H 'Content-Type: application/json'
```
#### Response Examples
```js
{
  "question": {
    "answer": "Blood",
    "category": "1",
    "difficulty": 4,
    "id": 3,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
- If request not provide JSON body:
```
```bash
curl -X POST http://127.0.0.1:5000/quizzes
```
```js
{
  "error": 400,
  "message": "Please provide quiz data.",
  "success": false
}
```