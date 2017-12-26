from model import Budget
from assertpy import assert_that
from datetime import date

def test_addIncome():
	assert_that(Budget({}).addIncome(8000)).contains_entry({"incomes":[{"income":8000, "title":"income", "desc":"", "date":date.today()}]})


def test_getBalanceRemaining():
	buget = Budget({})
	buget.addIncome(8000)
	buget.addBudget("candy", 500)
	buget.addBudget("eating", 2000)
	buget.addConsumption(50)

	assert_that(buget.getBalanceRemaining()).is_equal_to(7950)

def test_getBalanceAccountRemaining():
	buget = Budget({})
	buget.addIncome(8000)
	buget.addBudget("candy", 500)
	buget.addBudget("eating", 2000)
	buget.addConsumption(50, "candy")

	assert_that(buget.getBalanceAccountRemaining()).is_equal_to(5500)
