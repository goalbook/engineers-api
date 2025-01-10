import json

def lambda_handler(event, context):
    path = event['rawPath']  # '/engineers/1'
    parts = path.split('/')
    engineer_id = parts[-1] if len(parts) > 1 else None

    engineers = [
        {
            "_id": "0",
            "first_name": "Hain-Lee",
            "last_name": "Hsueh",
            "location": "California",
        },
        {
            "_id": "1",
            "first_name": "Malek",
            "last_name": "Ascha",
            "location": "Arizona",
        },
        {
            "_id": "2",
            "first_name": "Joy",
            "last_name": "Maloney",
            "location": "Massachusetts",
        },
        {
            "_id": "3",
            "first_name": "Sam",
            "last_name": "Pool",
            "location": "Colorado",
        },
        {
            "_id": "4",
            "first_name": "Eli",
            "last_name": "Zoller",
            "location": "South Carolina",
        },
        {
            "_id": "5",
            "first_name": "Keziyah",
            "last_name": "Lewis",
            "location": "Florida",
        },
        {
            "_id": "6",
            "first_name": "Suzanne",
            "last_name": "Li",
            "location": "New York",
        },
        {
            "_id": "7",
            "first_name": "Suzanne",
            "last_name": "Li",
            "location": "New York",
        },
        {
            "_id": "8",
            "first_name": "Ogochukwu",
            "last_name": "Ozotto",
            "location": "Texas",
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
            "body": json.dumps({"error": f"No engineer found with id '{engineer_id}'"})
        }
