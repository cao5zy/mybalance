import os
import itertools
from pymongo import MongoClient
from datetime import date

# schema defintion




class BudgetManagement:
	def __init__(self):
		from pymodm import connect, MongoModel, fields
		connect('mongodb://localhost:27017/testdb')

		class Income(MongoModel):
			income = fields.FloatField()
			desc = fields.CharField(min_length=0, max_length=255)
			date = fields.DateTimeField()
			title = fields.CharField(min_length=1, max_length=50)

		class Consumption(MongoModel):
			consumption = fields.FloatField()
			account = fields.CharField(min_length=1, max_length=125)
			date = fields.DateTimeField()
			desc = fields.CharField(min_length = 0, max_length=125)

		class Budget(MongoModel):
			account = fields.CharField(min_length = 1, max_length = 125)
			amount = fields.FloatField()

		class Balance(MongoModel):
			incomes = fields.EmbeddedDocumentListField(Income)
			consumptions = fields.EmbeddedDocumentListField(Consumption)
			bugdets = fields.EmbeddedDocumentListField(Budget)
			key = fields.CharField(min_length = 1, max_length = 50, primary_key = True, required = True)

		class Key(MongoModel):
			name = fields.CharField(min_length = 1, max_length = 20, primary_key = True)
			order = fields.IntegerField()
		# schema definition

		def currentKey(default="default"):
			return (lambda result: 0 if result.count() == 0 else result[0].order)(Key.objects.raw({"name": default}))
		def currentkey():
			pass

		def currentBalance():
			pass

		def currentBalance():
			pass

		def newBalance():
			#db["Balances"].insert_many([{"number": 1, "data": {"bds":[{"name": "KFC"}]}}])

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