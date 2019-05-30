import paramiko
import datetime
import os
##读取的脚本功能 1:巡检内容  2:负载状态
func=2
##读取当前路径
base_dir=os.getcwd()
##命令开始执行时间
starttime=datetime.datetime.now()
print(" -------------------------------------------------------------")
print("|                                                             |")
print("  startime:        ",starttime)
print("|                                                             |")
print(" -------------------------------------------------------------")
##注意路径前面的r，否则有些文件会当作转义字符处理
##读取命令脚本
if func==1:
    cmd_filepath=base_dir+r"\xunjian.txt"
else :
    cmd_filepath=base_dir+r"\fuzai.txt"
cmd_file=open(cmd_filepath,"r")
cmd=cmd_file.read()
##读取IP地址列表
ip_filepath=base_dir+r"\ip1.txt"
ip_file=open(ip_filepath,"r")
while 1:
    ipinfo=ip_file.readline()
    if not ipinfo :
        break
    else :
    ##读取IP，用户名，密码
         infos=ipinfo.split(',')
         host=infos[0]
         port = infos[1]
         username=infos[2]
         pwd=infos[3].strip()
         pwd=pwd.strip('\n')
    ##远程连接服务器
         client = paramiko.SSHClient()
         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         client.connect(host, port, username, pwd)
         stdin, stdout, stderr = client.exec_command(cmd)
         print(" -------------------------------------------------------------")
         print("|                                                             |")
         print("                      ",host)
         print("|                                                             |")
         print(" -------------------------------------------------------------")
         for line in stdout:
             print(line.strip('\n'))
         client.close()
         print("")
print('check complete................................')
##命令执行完成时间
endtime=datetime.datetime.now()
print(" -------------------------------------------------------------")
print("|                                                             |")
print("    endtime:      ",endtime)
print("|                                                             |")
print(" -------------------------------------------------------------")
print(" -------------------------------------------------------------")
print("|                                                             |")
print("  startime:       ",starttime)
print("  endtime:        ",endtime)
print("  cost:           ",endtime-starttime)
print("|                                                             |")
print(" -------------------------------------------------------------")