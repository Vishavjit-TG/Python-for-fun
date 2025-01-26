import requests

api_key = 'your_api_key'  # You need to sign up for an API key
mac_addresses = ['00:14:22:x:x:x', 'x:x:x:x:x:x']

def get_vendor(mac):
    url = f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('vendorDetails', {}).get('companyName', 'Vendor not found')
    else:
        return "Vendor not found"

for mac in mac_addresses:
    vendor = get_vendor(mac)
    print(f'MAC Address: {mac} -> Vendor: {vendor}')
