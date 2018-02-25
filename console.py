import sys
import datetime
from budget_management import BudgetManagement

def get_budget_param():
	return {
		"account": sys.argv[2]
		,"amount": sys.argv[3]
	}

def get_consumption_param():
	return {
		"account": sys.argv[2]
		,"consumption": sys.argv[3]
		,"desc": "" if len(sys.argv) == 4 else sys.argv[4]
	}

def get_income_param():
	return {
		"title": sys.argv[2]
		,"income": sys.argv[3]
		,"desc": "" if len(sys.argv) == 4 else sys.argv[4]
	}

def get_action():
	return sys.argv[2]

def add_budget():
	def add(budget_management):
		budget_management.add_budget(budget_management.currentBalance(), get_budget_param())

	add(BudgetManagement())

def add_consumption():
	def add(budget_management):
		budget_management.add_consumption(budget_management.currentBalance(), \
			get_consumption_param().update({"date": datetime.datetime.now()}))

	add(BudgetManagement())

def add_income():
	def add(budget_management):
		budget_management.add_income(budget_management.currentBalance(), \
			get_income_param().update({"date": datetime.datetime.now()}))

	add(BudgetManagement())

def error_cmd():
	print("error command")

def show_budget_remaining():
	import present
	def show(budget_management):
		present.showBudgetRemaining(budget_management.toJson(budget_management.currentBalance()))

	show(BudgetManagement())

def main():
	def process(action):
		(lambda actionDic:actionDic[(action if action in actionDic else "error_cmd").lower()]())\
		({
			"addbudget": add_budget
			,"addconsumption": add_consumption
			,"addincome": add_income
			,"errorcmd": error_cmd
			,"showbudgetremaining": show_budget_remaining
		})

	process(get_action())

if __name__ == '__main__':
	main()