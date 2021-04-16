import requests
import json
from datetime import datetime, timedelta



#TSHEETS
url = "https://rest.tsheets.com/api/v1/timesheets"

querystring = {
   "start_date": str((datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')),
}

payload = ""
headers = {
   'Authorization': "Bearer S.7__6114cfc1a82ed9afc75a0d4785da6b9b4d624a6a",
  }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


array  = response.text 

print(array)

data  = json.loads(array)




for key, val in data['results']['timesheets'].items():
	if val['user_id'] == 865293:
		val['user_id'] = 'LUIS ALFONSO RUIZ'
	elif val['user_id'] == 3043477:
		val['user_id'] = 'ALVARO GUINAND'
	elif val['user_id'] == 2993555:
		val['user_id'] = 'CORY SMITH'
	else:
		val['user_id'] == 3045093
		val['user_id'] = 'JAIRO ORTIZ CAMPO'

	inicio = val['start'].split('T')[1]

	print(val['user_id'] + ' is working has arrived to the job at  ' + inicio)














