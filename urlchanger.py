import json
def change(url):
        with open('client_secrets.json', 'r') as f:
            json_data = json.load(f)
        json_data['redirect_uris'] = url
        with open('my_file.json', 'w') as f:
            f.write(json.dumps(json_data))