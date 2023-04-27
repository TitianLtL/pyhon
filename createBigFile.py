
from datetime import datetime

header='PREV_EXTRACT_TS;CURR_EXTRACT_TS;CRUD_ACTION;DOMAIN;PAYLOAD\n'
com = '2021-07-01-11.00.00.123456;2021-07-01-12.00.00.123999;?;BS_GENERAL          ;'
dp1 = '{"TABLE":"POSTDISTRIKT ","DATA": {"POSTD_NR":"'
dp3 = '","LANDE_KODE_CHA_2":"TT","POSTD_ADR":"TORSHAVN","POSTD_SAEK_NR":100,"OPDAT_TID":"1996-09-11-15.54.05.142262","USERID":"    U082"}}'
cs  = '{"TOTAL_ROWS":       ?}'

number = 35000000

def createDataFile(name, size, line=''):
    deleteData(name)
    createFile(name, header)
    printLog("start loop :")
    for x in range(size):
        # line += com.replace('?', 'U') + dp1 + f'{x}' + dp3 + '\n'
        parts = [com.replace('?', 'U'), dp1, str(x), dp3, '\n']
        line = line + ''.join(parts)
        if x % 10000 == 0:
            createFile(name,line)
            line=''
    createFile(name, line)
    printLog("loop end   :")
    return line

def printLog(text):
    dt = datetime.now()
    print(text, dt)



def deleteData(name):
     open(name, 'w').close()


def createFile(name, data):
    with open(name, 'a') as f:
        f.write(data)

def createCSFile(name,size):
    deleteData(name)
    createFile(name, header)
    line = com.replace('?','S') + cs.replace('?',f'{size}')
    createFile(name, line)

if __name__ == "__main__":
    createDataFile("post_data2.txt",number)
    createCSFile ("post_cs.txt",number)

