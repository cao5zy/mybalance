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
			budgets = fields.EmbeddedDocumentListField(Budget)
			key = fields.CharField(min_length = 1, max_length = 50, primary_key = True, required = True)

		class Key(MongoModel):
			name = fields.CharField(min_length = 1, max_length = 20, primary_key = True, verbose_name = "name")
			order = fields.IntegerField()
		# schema definition

		def currentKey(name = "default"):
			return {
				"name": name,
				"order": (lambda result: 0 if result.count() == 0 else result[0].order)(Key.objects.raw({"_id": name}))
			}

		def setCurrentKey(keyObj):
			Key(name = keyObj["name"], order = keyObj["order"]).save()

			return currentKey(keyObj["name"])

		def increaseKey(keyObj):
			return {
				"name": keyObj["name"],
				"order": keyObj["order"] + 1
			}
		
		def decodeKey(keyObj):
			return "{name}-{order}".format(name = keyObj["name"], order = keyObj["order"])

		def newBalance(name = "default"):
			import datetime
			Balance(incomes = [Income(income = 0, \
					desc = 'default', \
					date = datetime.datetime.now(), \
					title = "income")], \
				consumptions = [Consumption(consumption = 0, \
					account = "None", \
					date = datetime.datetime.now(), \
					desc = "NA")], \
				budgets = [Budget(account = "None", \
					amount = 0)], \
				key = decodeKey(setCurrentKey(increaseKey(currentKey(name))))\
				).save()

		def currentBalance(name = "default"):
			return (lambda result:None if result.count() == 0 else result[0])\
				(Balance.objects.raw({"_id": decodeKey(currentKey(name))}))

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

		def addIncome(balance, incomeDict):
			balance.incomes.append(Income(income = incomeDict["income"], \
				desc = incomeDict["desc"], \
				date = incomeDict["date"], \
				title = incomeDict["title"]))
		self.newBalance = newBalance
		self.currentBalance = currentBalance
		self.historyBalances = historyBalances
		self.currentKey = currentKey
		self.setCurrentKey = setCurrentKey
		self.increaseKey = increaseKey
		self.addIncome = addIncome