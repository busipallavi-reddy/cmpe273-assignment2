from flask import Flask, escape, request, redirect, url_for, send_from_directory
from dbmodels import get_all_submissions, insert_submission, insert_test, fetch_test_keys, fetch_test
import os
import json

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SERVER_NAME'] = 'localhost:5000'

test_id = 1
tests = {}

def format_validation(content):
    keys_expected = ["subject", "answer_keys"]
    keys_actual = content.keys()
    for key in keys_actual:
        if key not in keys_expected:
            return False
    return True

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/tests', methods=['POST'])
def create_test():
    global test_id
    content = request.json
    if format_validation(content):
        entities = (test_id, content["subject"], json.dumps(content["answer_keys"]))
        insert_test(entities)
        test = {"test_id": test_id, "subject": content["subject"], "answer_keys": content["answer_keys"], "submissions": []}
        tests[str(test_id)] = 0
        test_id += 1
        return test, 201
    else:
        return "Bad Input Format", 400

@app.route('/api/tests/<int:test_id>/scantrons', methods=['POST'])
def upload_file(test_id):
    file = request.files.get("data")
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    scantron_url = url_for('uploaded_file', filename=filename, _external=True)
    f = open(UPLOAD_FOLDER + "/" + filename)
    content = json.load(f)
    answer_keys = json.loads(fetch_test_keys(test_id))
    answered_keys = content["answers"]
    result = {}
    score = 0
    for qno in answered_keys:
        result[qno] = {}
        result[qno]["actual"] = answered_keys[qno]
        result[qno]["expected"] = answer_keys[qno]
        if result[qno]["actual"] == result[qno]["expected"]:
            score += 1
    entities = (test_id, tests[str(test_id)]+1, str(scantron_url), content["name"], content["subject"], score, json.dumps(result))
    submission = {"scantron_id": tests[str(test_id)]+1, "scantron_url": scantron_url, "name": content["name"], \
                  "subject": content["subject"], "score": score, "result": result}
    insert_submission(entities)
    tests[str(test_id)] += 1
    return submission, 201

@app.route('/api/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test_details = fetch_test(test_id)
    submission_rows = get_all_submissions(test_id)
    response_obj = {"test_id": test_details[0], "subject": test_details[1], "answer_keys": json.loads(test_details[2]), "submissions": []}
    for submission in submission_rows:
        subm = {"scantron_id": submission[1], "scantron_url": submission[2],"name": submission[3], "subject": submission[4], \
                "score": submission[5], "result": json.loads(submission[6])}
        response_obj["submissions"].append(subm)
    return response_obj, 201

@app.route('/files/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)