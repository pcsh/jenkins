# -*- coding:utf-8 -*-

def get_variables(env = 'test'):
    if env=='product':
        #production environment
        variables = {
            #urlConfig
            "mainurl" : "http://main.com",
            #dbConfig
            "db_trade" : "tradeXXX",
            "db_trade_pw" : "12345678",
        }

    elif env=='exp':
    	#staging environment
        variables = {
            #urlConfig
            "mainurl" : "http://exp.main.com",
            #dbConfig
            "db_trade" : "trade_exp_XXX",
            "db_trade_pw" : "12345678",
        }

    else:
    	#text environment
        variables = {
            #urlConfig
            "mainurl" : "http://test.main.com",
            #dbConfig
            "db_trade" : "trade_test_XXX",
            "db_trade_pw" : "12345678",
        }
    globalvars = {'productid':'3456','userid':'test12'}   #共用变量
    variables['globalvars'] = globalvars

    return variables