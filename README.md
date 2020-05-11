# amp-connector-check

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/derak/amp-connector-check)

Check all endpoints to see if Cisco AMP connector was uninstalled

## Usage
- Add your `Client ID` and `API Key` to the `config` file. Instructions for getting these can be found here: https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1
- Add master list of hostnames to `master_endpoint_hostnames.txt`. If one of these hostnames does not show up in the list of hostnames queried from the AMP API, then it will alert. It will also alert if it sees one of the connector statuses is `inactive`.
- Run script
```
python amp_api.py
```

## Future Improvements
- Get master hostname list from Active Directory
- Send email when alerting
- Put in Docker continer
- Schedule runs, or keep persistent using `supervisord`
- Splunk integration
- Add support for Cisco Umbrella Roaming Client
