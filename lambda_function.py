import json
from urllib.parse import urlparse, unquote


def lambda_handler(event, context):
    path = event['rawPath']  # '/engineers/1'
    parts = path.split('/')
    engineer_id = parts[-1] if len(parts) > 1 else None

    engineers = [
        {
            "_id": "1",
            "first_name": "Hain-Lee",
            "last_name": "Hseuh",
            "location": "California",
            "start_date": "2000-01-01"
        },
    ]

    engineer = next((eng for eng in engineers if eng['_id'] == engineer_id), None)

    if engineer:
        return {
            "statusCode": 200,
            "body": json.dumps(engineer)
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"No engineer found with id {engineer_id}"})
        }
