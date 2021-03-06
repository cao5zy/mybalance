from datetime import date
from itertools import groupby

# def buildKey(obj, keyName, val):
# 	return obj if keyName in obj else buildOp(obj, lambda obj:obj[keyName]=val)

def buildOp(obj, handler):
	handler(obj)
	return obj


class Budget:
	"""docstring for budget"""
	def __init__(self, budgetObj):
		def addObj(name, obj):
			budgetObj.update({name: budgetObj[name] + [obj] if name in budgetObj \
				else [obj]})
			return budgetObj
		def getWithDefault(name, defaultVal = []):
			return budgetObj[name] if name in budgetObj else defaultVal

		def addIncome(amount, date = date.today(), title = "income", description = ""):
			return addObj("incomes", {"income": amount, "date": date, "desc": description, "title": title})

		def addConsumption(amount, account = "", date = date.today(), title = "", description = ""): 
			return addObj("consumptions", {"consumption": amount, "account": account, "date": date, "desc": description, })			

		def addBudget(account, amount): 
			# 添加预算账户
			return addObj("budgets", {"account": account, "amount": amount})

		def getSumOfConsumption():
			return sum(map(lambda obj:obj["consumption"], getWithDefault("consumptions")))

		def getSumOfIncome():
			return sum(map(lambda obj:obj["income"], getWithDefault("incomes")))

		def getBalanceRemaining():
			# 获取当前账期内的绝对余额
			return getSumOfIncome() - getSumOfConsumption()

		def getAccountConsumption():
			return dict([(key, sum(map(lambda x:x["consumption"], group))) for key, group in groupby(getWithDefault("consumptions"), lambda x:x["account"])])

		def getAccountBudget():
			return dict([(key, sum(map(lambda x:x["amount"], group))) for key, group in groupby(getWithDefault("budgets"), lambda x:x["account"])])

		def getBudgetRemaining():
			def getBudgetRemaining(accBudget, accCon):
				getRemaining = lambda key: accBudget[key] - accCon[key] if accBudget[key] - accCon[key] > 0 else 0
				return accBudget.update(dict(map(lambda key:(key, getRemaining(key)), \
				filter(lambda key:key in accCon, [key for key in accBudget])))) or accBudget

			return getBudgetRemaining(getAccountBudget(), getAccountConsumption())			
		def getBalanceAccountRemaining():
			# 获取账期内，扣除账户预算后的余额

			def getSumOfBudgetRemaining(budgetRemaining):
				return sum(map(lambda key:budgetRemaining[key], budgetRemaining))

			return getSumOfIncome() \
				- getSumOfConsumption() \
				- getSumOfBudgetRemaining(getBudgetRemaining())


		self.addConsumption = addConsumption
		self.addBudget = addBudget
		self.getBalanceRemaining = getBalanceRemaining
		self.getBalanceAccountRemaining = getBalanceAccountRemaining
		self.addIncome = addIncome
		self.getObj = lambda:budgetObj


def getAccountUsage(budgetId):
	# 获取当前账期内的账户使用情况
	pass

def getHistoryAccountUsage():
	# 获取历史的账户使用累计情况
	pass

def getCurrentBudgetId():
	# 获取当前账期号码
	pass
