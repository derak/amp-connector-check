import json
import requests
import configparser

# read api creds from config
config = configparser.ConfigParser()
config.read('config')
client_id = config['AMP']['ClientID']
api_key = config['AMP']['APIKey']

# master list of endpoint hostnames
master_endpoint_file = 'master_endpoint_hostnames.txt'

# amp api url and headers
url = 'https://api.amp.cisco.com/v1/computers'
headers = {'content-type': 'application/json --compressed', 'Accept-Encoding': 'gzip, deflate'}

def get_request():
    r = requests.get(url, headers=headers, auth=(client_id, api_key))
    body = json.loads(r.content)
    return body

def build_master_list():
    with open(master_endpoint_file) as f:
        master_endpoint_list = [line.rstrip('\n') for line in open(master_endpoint_file)]
    return master_endpoint_list


if __name__ == '__main__':

    master_endpoint_list = build_master_list()

    r = get_request()

    # loop through amp endpoint list and alert if status is inactive
    amp_connector_list = []
    for i in r['data']:
        if i['active'] == False:
            print('Alert!\nHostname: %s is inactive\nGUID: %s\n' % (i['hostname'], i['connector_guid']))
        amp_connector_list.append(i['hostname'])

    # if amp_connector_list is not the same as master list, alert for missing endpoints
    for i in master_endpoint_list:
        if i not in amp_connector_list:
            print('Alert!\nHostname: %s is inactive. Not found in AMP connector list.\n' % i)
