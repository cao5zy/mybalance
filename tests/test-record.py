# -*- coding: utf-8 -*- 
import record
from assertpy import assert_that
from datetime import date

def test_addSimple():
	result = record.addSimple("have lunch", 30)
	print(result)
	assert_that(result).contains_entry({"amount": 30})
	assert_that(result).contains_entry({"desc": 'have lunch'})
	assert_that(result["date"]).is_equal_to(date.today())
	assert_that(result["id"]).is_not_empty()

def test_getDefaultCategory():
	cat = record.getDefaultCategory('吃麦当劳')
	assert_that(cat).is_equal_to('吃')