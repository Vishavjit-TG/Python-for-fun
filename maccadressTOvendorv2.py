import requests
mac_addresses = ['x-x-x-x-x-x', .......]

def macvendors(mac):
  url = f"https://api.macvendors.com/{mac}"'
  response = requests.get{url}
  if response.status_code == 200:
    return response.text
  else:
    return "Vendor Not Found"

for mac in mac_address:
  vendor = macvenders(mac)
  print (f'MAC Address" {mac} ->  Vendors: {vendor}" ')

