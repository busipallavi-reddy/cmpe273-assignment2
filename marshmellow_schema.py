from marshmallow import Schema, fields
from  marshmallow.validate import OneOf

class CreateTestSchema(Schema):
    """ /api/tests - POST

    Parameters:
     - subject (str)
     - answer_keys (dict)
    """
    # the 'required' argument ensures the field exists

    options = ['A', 'B', 'C', 'D', 'E']
    qno = [str(i) for i in range(1, 51)]

    subject = fields.Str(required=True)
    answer_keys = fields.Dict(keys=fields.Str(required=True, validate=OneOf(qno)), \
                              values=fields.Str(required=True, validate=OneOf(options)))