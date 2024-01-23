import json

data = {
    'name' : 'Den',
    'shares' : '100',
    'count' : '523.23'
}

json_str = json.dumps(data)
with open(r"My project\work in file\data.json", "w") as f:
    json.dump(data, f)
    
