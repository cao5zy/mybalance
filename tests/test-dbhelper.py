# -*- coding: utf-8 -*-

import dbhelper
from datetime import date
from assertpy import assert_that

def test_insert():
	dbhelper.insert({"name":"曹", "date":date.today()})
	result = dbhelper.getAll()

	assert_that(result[0]['name']).is_equal_to('曹')