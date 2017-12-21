from datetime import date

# def buildKey(obj, keyName, val):
# 	return obj if keyName in obj else buildOp(obj, lambda obj:obj[keyName]=val)

def buildOp(obj, handler):
	handler(obj)
	return obj


class Budget:
	"""docstring for budget"""
	def __init__(self, budgetObj):
		def addIncome(amount, date = date.today(), title = "income", description = ""):
			def add(obj):
				budgetObj.update({"incomes": budgetObj["incomes"] + [obj] if "incomes" in budgetObj \
					else [obj]})
				return budgetObj

			return add({"income": amount, "date": date, "desc": description, "title": title})

		def addConsumption(account, amount, date = date.today(), title = "", description = ""): 
			# 添加消费
			pass

		def addBudget(account, amount): 
			# 添加预算账户
			pass

		def getBalanceRemaining():
			# 获取当前账期内的绝对余额
			pass

		def getBalanceAccountRemaining():
			# 获取账期内，扣除账户预算后的余额
			pass

		self.addConsumption = None;
		self.addBudget = None;
		self.getBalanceRemaining = None;
		self.getBalanceAccountRemaining = None;
		self.addIncome = addIncome;


def getAccountUsage(budgetId):
	# 获取当前账期内的账户使用情况
	pass

def getHistoryAccountUsage():
	# 获取历史的账户使用累计情况
	pass

def getCurrentBudgetId():
	# 获取当前账期号码
	pass
