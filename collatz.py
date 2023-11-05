import sys

def collatz(number):
  print(number)
  if number % 2 == 0:
    result = number//2
  elif number % 2 == 1:
    result = 3 * number + 1
  
  while result !=1:
    num = result
    return collatz(num)
  
  if result == 1:
    print(result)
    sys.exit()
  
def get_input():
  try:
    num = int(input())
    if num == 1:
      print('Your number: ',num)
      sys.exit()
    else:
      collatz(num)
  except ValueError:
    print('Integers only, please. Enter an integer')
    get_input()
    
print('Enter a number')
get_input()
  
