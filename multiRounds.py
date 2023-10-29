import time, sys

def runSession():
    session = 0
    sessionsTot = 5
    sesLen = 1
    restLen = 1
    
    while session < sessionsTot:
        session = session+1
        print('Go!')
        time.sleep(sesLen)
        if session < sessionsTot:
          print('Stop round ' + str(session) + '!')
          time.sleep(1)
        else:
          continue
  
    print('All done! Way to go!')

runSession()