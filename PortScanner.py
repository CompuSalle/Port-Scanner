# @Copyright
# Created by :
# Waseem Adel Alaa-Iddin
# Can be used in your project. A name maintaining will be nice.

import socket
import time
host = '10.0.2.15'
time_out = 1
stop =0
def onePort():

    sockProg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockProg.settimeout(time_out)
    runProg = sockProg.connect_ex((host, int(port)))

    if runProg == 0:
        print("Port '{}' At '{}' is -- Open ".format(port, host))
    else:
        print("Port '{}' At '{}' is -- Close ".format(port, host))
    sockProg.close()

def muliPort():
    for x in range(StartAt,StopAt):
                sockProg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sockProg.settimeout(time_out)
                runProg = sockProg.connect_ex((host, int(x)))
                if runProg == 0:
                    print("Port '{}' At '{}' is -- Open ".format(x, host))
                else:
                    print("Port '{}' At '{}' is -- Close ".format(x, host))
                sockProg.close()

try:
    while stop == 0:
        User_Scan = input('You wnat to Scan one port ? (Y/n)  >  ').lower()
    
        if User_Scan == 'y':
            try:

                port = input('\nWhat port you want to scan >> ')
                port = int(port)

                if port > 65535:
                    print('Port should be in range of 1 and 65535')
                    continue
                else:
                    onePort()
                    stop =+ 1
            except ValueError:
                print('\n[-] value Error, please enter number only')
                time.sleep()
                continue
                    
        elif User_Scan == 'n':
            try:
                StartAt = input('\nStart Range > > ')
                StopAt = input('\nStop Range > > ')

                StartAt = int(StartAt)
                StopAt = int(StopAt)
                StopAt += 1

                if StartAt >= StopAt:
                    print('\nStart cant be > stop')
                    time.sleep(1)
                    continue

                elif StartAt > 65535:
                    print('Port should be in range of 1 and 65535')
                    continue 
                 
                elif StopAt > 65535:
                    print('Port should be in range of 1 and 65535')
                    continue 

                else:
                    muliPort()
                    stop =+ 1


            except (ValueError, OverflowError) as error:
                print('\n[-] Error, please re-enter the values in range of 1 to 65535')
                time.sleep(1)
                continue
        else:
            print('[-] Only enter (y or n)')
            time.sleep(1)
            continue

except KeyboardInterrupt:
    print('[-] KeyboardInterrupt, Stopping')
    time.sleep()
    stop =+ 1


