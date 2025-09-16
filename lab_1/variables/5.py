#1
x = "best"

def a():
  print("KBTU the " + x)

a()

#2
x = "best"

def a():
  x = "top"
  print("KBTU the " + x)

a()

print("KBTU the " + x)

#3
def a():
  global x
  x = "top"

a()

print("KBTU the " + x)