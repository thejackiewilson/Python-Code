from turtle import color


x = "awesome"

def myfunc():
  global x
  print("Python is " + x)

myfunc()

print("w3 is " + x)

#global Keyword

def myfunc():
  global p
  p = "pushin"

myfunc()

print("My programming game is " + p) 