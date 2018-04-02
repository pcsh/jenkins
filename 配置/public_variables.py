# -*- coding:utf-8 -*-

JENKINS_URL = "http://172.16.11.54:9999/"
USERNAME = "cspan"
PASSWORD = "123456"

# 各个服务构建URL
ENT_FRONT_END_URL = "http://172.16.11.54:9999/job/ent-front-end/view/ms_build/"
SMARTCHECK_URL = "http://172.16.11.54:9999/job/smartcheck/view/ms_build/"
ES_SCK_SERVICE_URL = "http://172.16.11.54:9999/job/smartcheck/view/es-sck-service/"
BASE_SERVICE_URL = "http://172.16.11.54:9999/job/es/job/docker/view/base-service/"
ES_URL = "http://172.16.11.54:9999/job/es/job/docker/view/build-es/"

# 构建版本号
GIT_VERSION = "release-qybx-1.4.5"

# 默认环境及IP
BPC_ENV_NAME = "bpc"
BPC_SERVER_IP_27 = "172.16.11.27"
BPC_SERVER_IP_51 = "172.16.11.51"

TEST_ENV_NAME = "test"
TEST_SERVER_IP = "172.16.6.78"

BETA_ENV_NAME = "uat"
BETA_SERVER_IP = "172.16.202.3"
