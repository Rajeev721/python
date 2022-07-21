import requests

url = "https://login.microsoftonline.com/b1a63e20-bdda-4291-ada7-f059dcd07b14/oauth2/token"

payload='grant_type=client_credentials&client_id=7f77ed0f-3cca-4706-b108-0be60d3fbe42&client_secret=ci6gy.DdTE~pAF76qIv-eahX_rCD2T1A0Y&Resource=https%3A%2F%2Fmanagement.azure.com'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'fpc=AhvjAKcuc7lPqk4jPGayk1Z8bgNfAQAAAFTveNgOAAAAjqQYaQEAAACU73jYDgAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
}

response = requests.request("POST", url, headers=headers, data=payload)

a = dict(response.json())
access_token = a["access_token"]

print(access_token)