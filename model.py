from datetime import date

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

		def addIncome(amount, date = date.today(), title = "income", description = ""):
			return addObj("incomes", {"income": amount, "date": date, "desc": description, "title": title})

		def addConsumption(amount, account = "", date = date.today(), title = "", description = ""): 
			return addObj("consumptions", {"consumption": amount, "account": account, "date": date, "desc": description, })			

		def addBudget(account, amount): 
			# 添加预算账户
			return addObj("budgets", {"account": account, "amount": amount})

		def getSumOfConsumption():
			return sum(list(map(lambda obj:obj["consumption"], budgetObj["consumptions"] if "consumptions" in budgetObj else [])))

		def getSumOfIncome():
			return sum(list(map(lambda obj:obj["income"], budgetObj["incomes"] if "incomes" in budgetObj else [])))

		def getBalanceRemaining():
			# 获取当前账期内的绝对余额
			return getSumOfIncome() - getSumOfConsumption()

		def getBudgetConsumption():
			pass
			
		def getBalanceAccountRemaining():
			# 获取账期内，扣除账户预算后的余额
			def getBudgetRemaining():
				pass
			pass

		self.addConsumption = addConsumption
		self.addBudget = addBudget
		self.getBalanceRemaining = getBalanceRemaining
		self.getBalanceAccountRemaining = getBalanceAccountRemaining
		self.addIncome = addIncome


def getAccountUsage(budgetId):
	# 获取当前账期内的账户使用情况
	pass

def getHistoryAccountUsage():
	# 获取历史的账户使用累计情况
	pass

def getCurrentBudgetId():
	# 获取当前账期号码
	pass
