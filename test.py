# -*- coding: utf-8 -*-
import demjson

def main():
	result = demjson.decode_file('./data/2017-10-24.json')
	print(result[0]["name"])
if __name__ == '__main__':
	main()
