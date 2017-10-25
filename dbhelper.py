# -*- coding:utf-8 -*-
from datetime import date
import demjson
import jsondate
import json
import os
def insert(data):
	def writeToFile(fileName, jsonStr):
		with open(fileName, 'w', encoding='utf-8') as file:
			file.write(jsonStr)

	def appendData(json):
		json.append(data)
		return json

	(lambda fileName: writeToFile(fileName, jsondate.dumps((lambda json:appendData(json))\
		(demjson.decode_file(fileName, encoding='utf-8') if os.path.exists(fileName) else []))))(getName())


def getName():
	return './data/%s' % '{d.year}-{d.month}-{d.day}.json'.format(d=date.today())

def getAll():
	return demjson.decode_file(getName())
