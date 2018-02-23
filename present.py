from pipe import *

def genBudgetList(budgets):
	from itertools import groupby

	return [{"account": key, \
			"amount": sum(map(lambda n:n["amount"], group))
			} \
		for key, group in groupby(sorted(budgets, key = lambda n:n["account"]), lambda n:n["account"])]

def genConsumptionList(consumptions):
	from itertools import groupby

	return [{"account": key, \
			"consumption": sum(map(lambda n:n["consumption"], group))} \
		for key, group in groupby(sorted(consumptions, key = lambda n:n["account"]), lambda n:n["account"])]

def genResultList(budgets, consumptions):
	def cal(lst):
		from itertools import groupby
		return [{"account": key, \
			"amount": sum(map(lambda n:n["amount"], group))
			} \
			for key, group in groupby(sorted(lst, key=lambda n:n["account"]), lambda x:x["account"])]

	return cal([{"account": n["account"], \
		"amount": n["amount"]} for n in budgets] \
		+ [{"account": n["account"], \
		"amount": - n["consumption"]} for n in consumptions])

def printResult(resultList):
	from jinja2 import Template
	print(Template('''budgets remaining
budget\t\tremaining
{% for n in lst %}{{n.account}}\t\t{{n.amount}}
{% endfor %}''').render(lst = resultList))
def showBudgetRemaining(balance):
	printResult(\
		genResultList(\
			genBudgetList(balance["budgets"]), \
			genConsumptionList(balance["consumptions"]))\
		)
