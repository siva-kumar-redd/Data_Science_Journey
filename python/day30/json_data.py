import json
employee = {
    "id":101,
    "name":"Rahul",
    "salary":65000
}

json_data = json.dumps(employee,indent=4)

print(json_data)

