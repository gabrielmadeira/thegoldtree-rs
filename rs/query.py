import json
import requests

header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

data = {
  "title": "Um método para deduplicação de metadados bibliográficos baseado no empilhamento de classificadores",
  "abstract": " "
}

resp = requests.post("http://127.0.0.1:5000/rs", \
    data = json.dumps("Um método para deduplicação de metadados bibliográficos baseado no empilhamento de classificadores"),\
    headers= header)

# print(resp.status_code)

print(resp.json())