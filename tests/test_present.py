from assertpy import assert_that

def test_genBudgetList():
	from present import genBudgetList

	lst = [{
	"account": "play"
	,"amount": 30
	}
	,{
	"account": "play"
	,"amount": 40
	}]

	result = genBudgetList(lst)
	assert_that(result).is_length(1)
	assert_that(result[0]["amount"]).is_equal_to(70)
	assert_that(result[0]["account"]).is_equal_to("play")
