import paramiko
import datetime
import os



nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 年-月-日

# 时:分:秒
hourTime = datetime.datetime.now().strftime('%H:%M:%S')



dayTime = datetime.datetime.now().strftime('%Y-%m-%d')
pwd = os.getcwd() + '\\' + 'result' +'\\' + dayTime + '\\'
isExists = os.path.exists(pwd)
if not isExists:
    os.makedirs(pwd)