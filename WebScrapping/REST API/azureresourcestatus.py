import requests
from getbearertoken import access_token


url = "https://management.azure.com/subscriptions/0c93ece2-2ec8-4b64-b761-bbf337dd3dad/resourceGroups/azuresamplesub/providers/Microsoft.ResourceHealth/availabilityStatuses?api-version=2018-07-01"

payload={}
headers = {
  'Authorization': 'Bearer {}'.format(access_token)
}

# response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url, headers=headers, data=payload)
dict_status = response.json()
# print(dict_status)
# id = []
# status = []
# for i in range(len(dict_status["value"])):
#           id.append(dict_status["value"][i]['id'])
#           status.append(dict_status["value"][i]['properties']['availabilityState'])
# dict_upd = dict(zip(id,status))9

dict_upd = dict([[dict_status["value"][i]['id'],dict_status["value"][i]['properties']['availabilityState']] for i in range(len(dict_status["value"]))])
print(dict_status)
a = [[dict_status["value"][i]['id'],dict_status["value"][i]['properties']['availabilityState']] for i in range(len(dict_status["value"])) if dict_status["value"][i]['properties']['availabilityState'] != 'Available']

with open('D:\Learning\DataSet\sample.txt','w') as f:
  for i in range(len(dict_status["value"])):
          if dict_status["value"][i]['properties']['availabilityState'] not in ('Available','Unknown'):
                    f.write(str(dict_status["value"][i]['id'])+':'+ str(dict_status["value"][i]['properties']['availabilityState']) + ' and the reason is ' + str(dict_status["value"][i]['properties']['summary']))
                    f.write('\n')