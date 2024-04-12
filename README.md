# Django Robot Framework API

This project is a Django application that exposes an API endpoint for executing Robot Framework tests.

## Description

The core objective of this project is to create a system that can accept a detailed API call, execute the testing steps provided within as a Robot Framework test, and subsequently return the test output. This entails developing an application using Python and Django that exposes an API endpoint. This endpoint accepts a POST request structured as follows, executes the detailed steps using the Robot Framework, and returns the results.

## Installation

Clone the repository and navigate into the project directory. Install the required dependencies.

```bash
git clone https://github.com/Urmila4718/robot_test_project
cd robot_test_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Usage

To use this application, send a POST request to the `/execute_test` endpoint with a JSON body containing the tests to be executed. Each test should be a dictionary with a 'title' and a list of 'steps'.

Here's an example of a valid request:

```json


{
 "tests":[
 {
 "title":"Open google.com",
 "steps":[
 "Open Browser browser='chrome'",
 "Go To url='https://google.com'"
 ]
 }
 ]
}

data = {
    "tests": [
        {
            "title": "Open google.com",
            "steps": [
                "Open Browser browser='chrome'",
                "Go To url='https://google.com'"
            ]
        }
    ]
}

response = requests.post(url, json=data)
print(response.json())