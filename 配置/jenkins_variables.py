# -*- coding:utf-8 -*-

def get_variables(env = 'test', app = 'ent_front_end'):
    if env=='bpc':
        #bpc环境报销前台
        variables = {
	    "BUILD_URL":"http://172.16.11.54:9999/job/ent-front-end/view/ms_build/",
	    "GIT_VERSION":"release-qybx-1.4.4",
            "ENV_NAME" : "bpc",
            "SERVER_IP" : "172.16.11.51",
        }

    elif env=='beta':
    	#beta环境报销前台
        variables = {
	    "BUILD_URL":"http://172.16.11.54:9999/job/ent-front-end/view/ms_build/",
	    "GIT_VERSION":"release-qybx-1.4.4",
            "ENV_NAME" : "uat",
            "SERVER_IP" : "172.16.202.3",
        }

    else:
    	#test环境报销前台
        variables = {
	    "BUILD_URL":"http://172.16.11.54:9999/job/ent-front-end/view/ms_build/",
	    "GIT_VERSION":"release-qybx-1.4.4",
            "ENV_NAME" : "test",
            "SERVER_IP" : "172.16.11.56",
        }

    return variables