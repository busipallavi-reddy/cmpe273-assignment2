# cmpe273-assignment2


* dbmodels.py is the script containing the SQLite3 connection and db models. It has all the create, select and delete functions.

* tests.db is the database dump for the DB tests. The DB contains 2 tables - test and submissions.
   * test - test_id integer PRIMARY KEY, subject text, answer_keys text
   * submissions - CREATE TABLE submissions(test_id integer, scantron_id integer, scantron_url text, name text, subject text, score integer, result text, PRIMARY KEY(test_id, scantron_id)     

* marshmallow_schema.py has the Marshmallow Schema to validate input for Create Test API and Upload Scantron API.
   
* app.py on every start, creates connection to tests.db and cleanups any previous data. It also validates the JSON input on create test and upload scantron API using the above marshmallow schemas.

* files/ folder - All the uploaded files are store here.

* The files are downloadable by doing a GET request on the scantron_url returned.

