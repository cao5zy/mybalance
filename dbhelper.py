# -*- coding:utf-8 -*-
from datetime import date
import demjson
import jsondate
import os
def insert(data):
	def writeToFile(fileName, json):
		with open(fileName, 'w') as file:
			file.write(jsondate.dumps(json))

	def appendData(json):
		json.append(data)
		return json

	(lambda fileName: writeToFile(fileName, (lambda json:appendData(json))\
		(demjson.decode_file(fileName) if os.path.exists(fileName) else [])))(getName())


def getName():
	return './data/%s' % '{d.year}-{d.month}-{d.day}.json'.format(d=date.today())