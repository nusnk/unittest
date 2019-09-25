def fooBar(number):
    number_str = str(number)
    if number % 3 is 0 or '3' in number_str:
        print("Foo")
    elif number % 5 is 0 or '5' in number_str:
        print("Bar")
    elif number % 7 is 0 or '7' in number_str:
        print("Qix")
    else:
        print(number)
