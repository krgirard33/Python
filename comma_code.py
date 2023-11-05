# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. 
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it. 
# Be sure to test the case where an empty list [] is passed to your function.


def create_string(inward):
  line = ''
  for index, item in enumerate(inward):
    if len(inward) < 2:
      line = line + str(item)
    elif index == len(inward)-1:
      line = line + ", and " + str(item)
    elif index > 0:
      line = line + ", " + str(item)
    else:
      line = line + str(item)
  
  return line
      
spam = ['apples', 10, 'bananas', 'tofu', 'cats']
print(create_string(spam))