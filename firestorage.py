import json
import urequests
import random
import time

def bratzinai(collection, temp):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWQYZ"
    id = "".join(random.choice(letters) for _ in range(20))  # Fixed the ID length to 20
    date_now_to_post = int(time.time())  # Convert the timestamp to an integer
    print('DOCUMENT ID CREATED')

    sample_data = {
        "temperature": {
            "integerValue": temp["temperature"] # Fixed the temperature key
        },
        "date": {
            "timestampValue": "22:01"  # Fixed the timestamp key
        }
    }

    print('init Firebase API function')
    project_id = "chameleon-test-3ec1f"
    location = f"projects/{project_id}/databases/(default)/documents/{collection}/{id}"
    url = f"https://firestore.googleapis.com/v1/{location}"
    headers = {
        "Content-Type": "application/json"
    }

    document_data = {
        "fields": sample_data
    }

    try:
        print('init request to Firestore API...')
        response = urequests.patch(url, data=json.dumps(document_data), headers=headers)
        if response.status_code == 200:
            print("--> Data pushed successfully!!")
            print("--> status code:", response.status_code)
        else:
            print('--> ERROR: can not push data')
            print('--> status code: ', response.status_code)
            print(response.json())
    except Exception as e:
        print('Cannot upload data:', e)

