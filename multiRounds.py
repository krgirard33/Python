import time, sys

def run_session():
    session = 0
    sessions_tot = 5
    ses_len = 30
    rest_len = 10
    
    while session < sessions_tot:
        session = session+1
        print('Go!')
        time.sleep(ses_len)
        if session < sessions_tot:
          print('Stop round ' + str(session) + '!')
          time.sleep(rest_len)
        else:
          continue
  
    print('All done! Way to go!')

run_session()