from budget_management import BudgetManagement
from assertpy import assert_that
import datetime

def test_currentBudget():
		budgetManagement = BudgetManagement()
		budgetManagement.newBalance()

		currentBalance = budgetManagement.currentBalance()
		assert_that(currentBalance.incomes).is_length(1)
		assert_that(currentBalance.consumptions).is_length(1)
		assert_that(currentBalance.budgets).is_length(1)

		budgetManagement.addIncome(currentBalance, {
			"income": 7400,
			"desc": "salary",
			"date": datetime.datetime.now(),
			"title": "salary"
			})
		currentBalance.save()

		currentBalance = budgetManagement.currentBalance()
		assert_that(currentBalance.incomes).is_length(2)

def test_currentKey():
	budgetManagement = BudgetManagement()

	result = budgetManagement.currentKey()

	assert_that(budgetManagement.setCurrentKey(budgetManagement.increaseKey(result))["order"]).is_equal_to(result["order"] + 1)
