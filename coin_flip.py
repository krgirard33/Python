import random
numberOfStreaks = 0
numberOfRounds = 0
    
for experimentNumber in range(10000):
  paper = ''
  numberOfRounds += 1
  # Code that creates a list of 100 'heads' or 'tails' values.
  for flips in range(100):
    coin = random.randint(0,1)
    paper += str(coin)

  # Code that checks if there is a streak of 6 heads or tails in a row.
  heads = '000000'
  tails = '111111'
  
  if paper !=None and heads in paper or tails in paper:
    numberOfStreaks += 1  
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfRounds, numberOfStreaks)