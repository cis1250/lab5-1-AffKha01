#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def user_input():
  while (True):
    print("Please enter the number of terms")
    terms = input()
    if (terms.isdigit()):
        terms = int(terms)
        if (terms > 0):
          break;
        else:
          print("Incorrect input, please input a integer greater than 0")
    else:
      print("Incorrect input, please input an integer greater than 0")
  return terms

def fibonacci (terms):
  if (terms == 0):
    return 0
  if (terms == 1):
    return 0
  elif (terms == 2):
    return 1
  else:
    return fibonacci(terms - 1) + fibonacci (terms - 2)

def print_fib (terms):
  for i in range (1, terms + 1):
    print(fibonacci(i), end= " ")
  
terms = user_input()
fibonacci(terms)
print_fib(terms)
