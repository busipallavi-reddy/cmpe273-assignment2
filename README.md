# cmpe273-assignment2


* dbmodels.py is the script containing the SQLite3 connection and db models. It has all the create, select and delete functions.

* tests.db is the database dump for the DB tests. The DB contains 2 tables - test and submissions.
   * test - test_id integer PRIMARY KEY, subject text, answer_keys text
   * submissions - CREATE TABLE submissions(test_id integer, scantron_id integer, scantron_url text, name text, subject text, score integer, result text, PRIMARY KEY(test_id, scantron_id)     

* marshmallow_schema.py has the Marshmallow Schema to validate input for Create Test API and Upload Scantron API.
  
* app.py on every start, creates connection to tests.db and cleanups any previous data. It also validates the JSON input on create test and upload scantron API using the above marshmallow schemas.

* files/ folder - All the uploaded files are store here.

* The uploaded files are downloadable by doing a GET request on the scantron_url returned.

* Postman/cmpe273-assignment2.postman_collection.json - The Postman collection



## Installation and Execution

* Installing sqlite and sqlite browser

  ```
  $ sudo apt-get update
  $ sudo apt-get install sqlite3
  $ sudo apt-get install sqlitebrowser
  ```

* Installing pipenv, flask, marshmallow, sqlite3

  ```
  pip install pipenv
  
  pipenv install flask==1.1.1
  
  pip install sqlite3
  
  pip install marshmallow
  
  pipenv shell
  ```

* Run app.py 

  ```
  env FLASK_APP=app.py flask run
  ```

  

# APIs

## Create a test

*Request*

>  POST <http://localhost:5000/api/tests>

```
{
    "subject": "Math",
    "answer_keys": {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "A",
        "6": "B",
        "7": "C",
        "8": "D",
        "9": "A",
        "10": "B",
        "11": "A",
        "12": "B",
        "13": "C",
        "14": "D",
        "15": "A",
        "16": "B",
        "17": "C",
        "18": "D",
        "19": "A",
        "20": "B",
        "21": "A",
        "22": "B",
        "23": "C",
        "24": "D",
        "25": "A",
        "26": "B",
        "27": "C",
        "28": "D",
        "29": "A",
        "30": "B",
        "31": "A",
        "32": "B",
        "33": "C",
        "34": "D",
        "35": "A",
        "36": "B",
        "37": "C",
        "38": "D",
        "39": "A",
        "40": "B",
        "41": "A",
        "42": "B",
        "43": "C",
        "44": "D",
        "45": "A",
        "46": "B",
        "47": "C",
        "48": "D",
        "49": "A",
        "50": "B"
    }
}
```

*Response*

```
201 Created

{
    "answer_keys": {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "A",
        "6": "B",
        "7": "C",
        "8": "D",
        "9": "A",
        "10": "B",
        "11": "A",
        "12": "B",
        "13": "C",
        "14": "D",
        "15": "A",
        "16": "B",
        "17": "C",
        "18": "D",
        "19": "A",
        "20": "B",
        "21": "A",
        "22": "B",
        "23": "C",
        "24": "D",
        "25": "A",
        "26": "B",
        "27": "C",
        "28": "D",
        "29": "A",
        "30": "B",
        "31": "A",
        "32": "B",
        "33": "C",
        "34": "D",
        "35": "A",
        "36": "B",
        "37": "C",
        "38": "D",
        "39": "A",
        "40": "B",
        "41": "A",
        "42": "B",
        "43": "C",
        "44": "D",
        "45": "A",
        "46": "B",
        "47": "C",
        "48": "D",
        "49": "A",
        "50": "B"
    },
    "subject": "Math",
    "submissions": [],
    "test_id": 1
}
```

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/create_test_1.png)

Marshmallow Schema validation is also done and errors are shown in the following screenshot.

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/create_test_invalid_json.png)

## 

## Upload a scantron

*Request*

> POST <http://localhost:5000/api/tests/1/scantrons>

```
curl -F 'data=@scantron-1.json' http://localhost:5000/api/tests/1/scantrons
```

*Response*

```
201 Created

{
    "scantron_id": 1,
    "scantron_url": "http://localhost:5000/files/scantron-1.json",
    "name": "Foo Bar",
    "subject": "Math",
    "score": 40,
    "result": {
        "1": {
            "actual": "A",
            "expected": "B"
        },
        "..": {
            "actual": "..",
            "expected": ".."
        },
        "50": {
            "actual": "E",
            "expected": "E"
        }
    }
}
```

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/upload_scantron_1.png)

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/upload_scantron_2.png)

The scantron URL is downloadable as seen below in the screenshot - 

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/downlaod_scantron.png)

Marshmallow Schema validation is also done and errors are shown in the following screenshot.

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/upload_file_invalid_json.png)



## Check all scantron submissions

*Request*

> GET <http://localhost:5000/api/tests/1>

*Response*

```
{
    "answer_keys": {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "A",
        "6": "B",
        "7": "C",
        "8": "D",
        "9": "A",
        "10": "B",
        "11": "A",
        "12": "B",
        "13": "C",
        "14": "D",
        "15": "A",
        "16": "B",
        "17": "C",
        "18": "D",
        "19": "A",
        "20": "B",
        "21": "A",
        "22": "B",
        "23": "C",
        "24": "D",
        "25": "A",
        "26": "B",
        "27": "C",
        "28": "D",
        "29": "A",
        "30": "B",
        "31": "A",
        "32": "B",
        "33": "C",
        "34": "D",
        "35": "A",
        "36": "B",
        "37": "C",
        "38": "D",
        "39": "A",
        "40": "B",
        "41": "A",
        "42": "B",
        "43": "C",
        "44": "D",
        "45": "A",
        "46": "B",
        "47": "C",
        "48": "D",
        "49": "A",
        "50": "B"
    },
    "subject": "Math",
    "submissions": [
        {
            "name": "Foo Bar",
            "result": {
                "1": {
                    "actual": "A",
                    "expected": "A"
                },
                "2": {
                    "actual": "B",
                    "expected": "B"
                },
                "3": {
                    "actual": "C",
                    "expected": "C"
                },
                "4": {
                    "actual": "D",
                    "expected": "D"
                },
                "5": {
                    "actual": "A",
                    "expected": "A"
                },
                "6": {
                    "actual": "B",
                    "expected": "B"
                },
                "7": {
                    "actual": "C",
                    "expected": "C"
                },
                "8": {
                    "actual": "D",
                    "expected": "D"
                },
                "9": {
                    "actual": "A",
                    "expected": "A"
                },
                "10": {
                    "actual": "B",
                    "expected": "B"
                },
                "11": {
                    "actual": "A",
                    "expected": "A"
                },
                "12": {
                    "actual": "B",
                    "expected": "B"
                },
                "13": {
                    "actual": "C",
                    "expected": "C"
                },
                "14": {
                    "actual": "D",
                    "expected": "D"
                },
                "15": {
                    "actual": "A",
                    "expected": "A"
                },
                "16": {
                    "actual": "B",
                    "expected": "B"
                },
                "17": {
                    "actual": "C",
                    "expected": "C"
                },
                "18": {
                    "actual": "D",
                    "expected": "D"
                },
                "19": {
                    "actual": "A",
                    "expected": "A"
                },
                "20": {
                    "actual": "B",
                    "expected": "B"
                },
                "21": {
                    "actual": "A",
                    "expected": "A"
                },
                "22": {
                    "actual": "B",
                    "expected": "B"
                },
                "23": {
                    "actual": "E",
                    "expected": "C"
                },
                "24": {
                    "actual": "D",
                    "expected": "D"
                },
                "25": {
                    "actual": "A",
                    "expected": "A"
                },
                "26": {
                    "actual": "B",
                    "expected": "B"
                },
                "27": {
                    "actual": "C",
                    "expected": "C"
                },
                "28": {
                    "actual": "D",
                    "expected": "D"
                },
                "29": {
                    "actual": "A",
                    "expected": "A"
                },
                "30": {
                    "actual": "A",
                    "expected": "B"
                },
                "31": {
                    "actual": "A",
                    "expected": "A"
                },
                "32": {
                    "actual": "B",
                    "expected": "B"
                },
                "33": {
                    "actual": "C",
                    "expected": "C"
                },
                "34": {
                    "actual": "D",
                    "expected": "D"
                },
                "35": {
                    "actual": "A",
                    "expected": "A"
                },
                "36": {
                    "actual": "B",
                    "expected": "B"
                },
                "37": {
                    "actual": "C",
                    "expected": "C"
                },
                "38": {
                    "actual": "D",
                    "expected": "D"
                },
                "39": {
                    "actual": "A",
                    "expected": "A"
                },
                "40": {
                    "actual": "B",
                    "expected": "B"
                },
                "41": {
                    "actual": "A",
                    "expected": "A"
                },
                "42": {
                    "actual": "B",
                    "expected": "B"
                },
                "43": {
                    "actual": "C",
                    "expected": "C"
                },
                "44": {
                    "actual": "D",
                    "expected": "D"
                },
                "45": {
                    "actual": "A",
                    "expected": "A"
                },
                "46": {
                    "actual": "B",
                    "expected": "B"
                },
                "47": {
                    "actual": "C",
                    "expected": "C"
                },
                "48": {
                    "actual": "D",
                    "expected": "D"
                },
                "49": {
                    "actual": "A",
                    "expected": "A"
                },
                "50": {
                    "actual": "B",
                    "expected": "B"
                }
            },
            "scantron_id": 1,
            "scantron_url": "http://localhost:5000/files/scantron-1.json",
            "score": 48,
            "subject": "Math"
        }
    ],
    "test_id": 1
}
```

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/get_test_submissions_1.png)

![](https://github.com/busipallavi-reddy/cmpe273-assignment2/blob/master/Postman/get_test_submissions_2.png)
