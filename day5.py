def main():
    x = get_int("number daalo: ")
    print(f"x is {x}")
def get_int(prompt):    
    while True:
      try:
          x = int(input(prompt))
          return x
      except ValueError:
          pass
      
main()      