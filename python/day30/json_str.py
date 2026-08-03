import json
student = {
    "name": "Siva",
    "age": 22
}

json_data = json.dumps(student)
print(json_data)