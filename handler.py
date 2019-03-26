import json

from gluoncv.data.transforms.presets.ssd import load_test
from gluoncv.model_zoo import get_model

def detect(event, context):

    body = {
        "imoport ok"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
