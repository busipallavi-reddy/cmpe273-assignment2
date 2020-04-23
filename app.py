from flask import Flask, escape, request
from dbmodels import get_all_submissions, insert_submission, insert_test, fetch_test_keys, fetch_test

import json

app = Flask(__name__)

test_id = 1
tests = {}

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/tests', methods=['POST'])
def create_test():
    global test_id
    content = request.json
    entities = (test_id, content["subject"], json.dumps(content["answer_keys"]))
    insert_test(entities)
    test = {"test_id": test_id, "subject": content["subject"], "answer_keys": content["answer_keys"], "submissions": []}
    tests[str(test_id)] = 0
    test_id += 1
    return test, 201

@app.route('/api/tests/<int:test_id>/scantrons', methods=['POST'])
def upload_test(test_id):
    content = request.json
    answer_keys = json.loads(fetch_test_keys(test_id))
    answered_keys = content["answered_keys"]
    result = {}
    score = 0
    for qno in answered_keys:
        result[qno] = {}
        result[qno]["actual"] = answered_keys[qno]
        result[qno]["expected"] = answer_keys[qno]
        if result[qno]["actual"] == result[qno]["expected"]:
            score += 1
    entities = (test_id, tests[str(test_id)]+1, content["name"], content["subject"], score, json.dumps(result))
    submission = {"test_id": test_id, "scantron_id": tests[str(test_id)]+1, "name": content["name"], \
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
        subm = {"scantron_id": submission[1], "name": submission[2], "subject": submission[3], \
                "score": submission[4], "result": json.loads(submission[5])}
        response_obj["submissions"].append(subm)
    return response_obj, 201