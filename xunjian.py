# 作者：wjq   
# 创建时间: 2019/5/15  
# 文件: app.py.py   
# 软件名称: PyCharm

import paramiko
import threading


# 获取服务器信息表
def get_host():
    file = open(r'host.txt')
    for line in file:
        linelist = line.split(',')
        ip = linelist[0]
        username = linelist[1]
        pwd = linelist[2]
        port_num = linelist[3]
        connect_server(ip, username, pwd, port_num)


# 进行巡检
def connect_server(ip, username, pwd, port_num):
    #try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port_num, username, pwd, timeout=20)

        """显示返回结果使用内存"""
        # 使用内存
        stdin, stdout1, stderr = ssh.exec_command(
            "free -m |awk 'NR==2' |awk '{ print $3}'")
        out1 = stdout1.readlines()
        print(ip + "：" + "使用内存" + out1[0])

        # 剩余内存
        stdin, stdout2, stderr = ssh.exec_command(
            "free -m |awk 'NR==2' |awk '{ print $4}'")
        out2 = stdout2.readlines()
        print(ip + "：" + "剩余内存" + out2[0])

        #内存判断
        a=("%.2f%%" %(int(out1[0])/int(out2[0])*100))
        b=("%2.f%%" %(90/100*100))

        if a > b:
            print("内存不足:" + ip + ',' + '使用内存'+ out1[0])
        else:
            print("xxxx")

        # CPU
        stdin, stdout3, stderr = ssh.exec_command(
            """ su - oracle | sqlplus /nolog  |select table_name from user_tables;  """)

        out3 = stdout3.readlines()
        print(out3)


    #except:
    #    print("ssdfsdf")


if __name__ == "__main__":
    t = threading.Thread(target=get_host)
    t.start()
    input()










