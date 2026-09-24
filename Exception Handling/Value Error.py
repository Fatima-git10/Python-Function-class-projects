try:
    number=int(input("enter a number: "))
    print(number)
except ValueError as ve:
    print(ve)