import requests
import json

file = open('ipv6_oc.csv', 'r')

cont = 0
while True:
    line = file.readline()

    if not line:
        break

    cont += 1
    id = line.strip()
    print(cont)

    url = "https://services.nvd.nist.gov/rest/json/cve/1.0/" + id

    headers = {
        'apiKey': 'b40416e7-2366-4a7f-9a83-e57962dd926f'
    }

    response = requests.request("GET", url, headers=headers)
    
    response_json = response.json()
    #print(response_json)
    
    response_string = json.dumps(response_json)
    
    output = './output-ipv6/' + id + '.json'

    with open(output, 'w') as outfile:
        outfile.write(response_string)

file.close()