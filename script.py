import requests
import json
from datetime import datetime, timedelta
import csv
import smtplib, ssl
import os
from os import environ
from apscheduler.schedulers.blocking import BlockingScheduler




sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('This job is run every five minutes.')

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



	data  = json.loads(array)
	print(data['results']['timesheets'])
	message = ''
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

		inicio = val['start'].split('T')[1].split('-')[0]
		fin = val['end'].split('T')[1].split('-')[0]
		horas_trabajadas = round(val['duration']/3600, 2)

		message =  message + val['user_id'] + ' arrived today at work at  ' + inicio + ' and left at ' + fin + ' having worked for '+ str(horas_trabajadas) + ' hours \n'
		
	print(message)

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "leasingibericmalls@gmail.com"  # Enter your address
	email = 'geronimoalonso@icloud.com'
	password = 'guwHer-zuwsi7-rusres'
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, email, message)

	 
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "leasingibericmalls@gmail.com"  # Enter your address
	email = 'admin@ibericmalls.com'
	password = 'guwHer-zuwsi7-rusres'
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, email, message)






sched.start()


	# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
	# def scheduled_job():
	#     print('This job is run every weekday at 5pm.')


