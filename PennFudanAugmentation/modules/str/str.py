#!/usr/bin/env python3
#-*- coding:utf-8 -*- HWY

def IsContainSub2(str,subStr):
	return subStr in str
	
def IsContainSub(str,subStr):
	return str.find(subStr) != -1
	