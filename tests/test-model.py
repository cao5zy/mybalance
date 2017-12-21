from model import Budget
from assertpy import assert_that
from datetime import date

def test_addIncome():
	assert_that(Budget({}).addIncome(8000)).contains_entry({"incomes":[{"income":8000, "title":"income", "desc":"", "date":date.today()}]})


def test_addConsumption():
	pass

def test_addBudget():
	pass

def test_getBalanceRemaining():
	pass

def test_getBalanceAccountRemaining():
	pass