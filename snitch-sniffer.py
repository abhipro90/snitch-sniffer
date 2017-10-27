me=input("What is your name?")
print("Hello", name)

def times_tables(num, how_many):
    n=1
    while n<=how_many:
      print(num, " x ", n, "=", num*n)
      n=n+1
def powerOf(num,power):
    if power == 2:
      return num*num
    else:
      return num*num*num
