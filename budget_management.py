import os
import itertools
from pymongo import MongoClient
from datetime import date

# schema defintion
from mongorm import Field, Database
db = Database(uri='mongodb://localhost:27017/testdb')

class MyBalance(db.Document):
	__collection__ = "MyBalances"
	__fields__ = {
		"incomes": [{
			"income": Field.required(float),
			"date": Field.required(date),
			"desc": Field.optional(str),
			"title": Field.required(str)
		}],
		"budgets": [{
			"account": Field.required(str),
			"amount": Field.required(float)
		}],
		"consumptions": [{
			"consumption": Field.required(str),
			"account": Field.required(str),
			"date": Field.required(date),
			"desc": Field.optional(str)
		}],
		"key": Field.required(int)
	}

class Key(db.Document):
	__collection__ = "Keys"
	__fields__ = {
		"name": Field.required(str),
		"order": Field.required(int)
	}


class BudgetManagement:
	def __enter__(self):
		return self

	def __exit__(self, e_t, e_v, t_b):
		self.conn.close()

	def __init__(self):
		self.conn = MongoClient("mongodb://localhost", 27017)
		db = self.conn.testdb

		def currentKey(default="default"):
			def findKey(col):
				print(col)
				print(col.count())
				return 0 if not col else col.find({name: default}).value
			return findKey(db["keys"])

		def currentkey():
			pass

		def currentBalance():
			pass

		def currentBalance():
			pass

		def newBalance():
			db["Balances"].insert_many([{"number": 1, "data": {"bds":[{"name": "KFC"}]}}])

			# generate a new balance with name number-date.json
			pass

		def currentBalance():
			print(loadAllBalancesFileName())
			# if the folder is empty, return None
			pass

		def historyBalances():
			pass

		def loadAllBalancesFileName():
			pass

		def getFileNameParts(fileName):
			def processName(exp):
				if not re.search(exp, fileName):
					raise Error("invalid file name:%s" % fileName)
				
		def getNumberOfFileName(fileName):
			pass

		def getDateOfFileName(fileName):
			pass

		self.newBalance = newBalance
		self.currentBalance = currentBalance
		self.historyBalances = historyBalances
		self.currentKey = currentKey