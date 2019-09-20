from os import listdir
from os import path
from datetime import datetime, timedelta
from os import system

backupFolder = "/"      #đường dẫn tới thư mục backup VD: /etc/redmine/backup/ kết thúc bằng dấu /
listFileFolder = ""
today = datetime.now()
#Định dạng ngày hôm qua
yesterday = datetime.strftime(today - timedelta(1),"%Y%m%d")

#Kiểm tra xem có file hay ko
def checkFileExist(day):
    for i in listFileFolder:
        if day in i:
            return True

#Gửi mail cảnh báo
def sendMail():
    cmd = "echo \"Backup is not successful\" | mail -s \"Backup Problem\" thang.tran1@ntq-solution.com.vn"
    system(cmd)

#Kiểm tra xem có thư mục hay ko
def checkFolderExist(arg):
    if path.exists(arg):
        return True
    return False

#main
print("Yesterday: " + yesterday)
directory = backupFolder+str(yesterday)
print("Checking backup directory: " + directory)
if checkFolderExist(directory):
    print("Backup Folder exist, OK!")
    listFileFolder = listdir(directory)
    if checkFileExist("tar.gz"):
        print("Backup File exist, OK!")
    else:
        print("No backup File, FAIL!")
        sendMail()
else:
    print("No backup Folder, FAIL!")
    sendMail()
