from budget_management import BudgetManagement
from assertpy import assert_that
import datetime

def test_currentBudget():
		budgetManagement = BudgetManagement()
		budgetManagement.new_balance()

		current_balance = budgetManagement.current_balance()
		assert_that(current_balance.incomes).is_length(1)
		assert_that(current_balance.consumptions).is_length(1)
		assert_that(current_balance.budgets).is_length(1)

		budgetManagement.add_income(current_balance, {
			"income": 7400,
			"desc": "salary",
			"date": datetime.datetime.now(),
			"title": "salary"
			})
		budgetManagement.add_consumption(current_balance, {
			"consumption": 50,
			"account": "play",
			"date": datetime.datetime.now(),
			"desc": "play"
			})
		budgetManagement.add_budget(current_balance, {
			"account": "play",
			"amount": 1200
			})

		current_balance.save()

		current_balance = budgetManagement.current_balance()
		assert_that(current_balance.incomes).is_length(2)
		assert_that(current_balance.consumptions).is_length(2)
		assert_that(current_balance.budgets).is_length(2)

def test_currentKey():
	budgetManagement = BudgetManagement()

	result = budgetManagement.current_key()

	assert_that(budgetManagement.set_current_key(budgetManagement.increase_key(result))["order"]).is_equal_to(result["order"] + 1)
