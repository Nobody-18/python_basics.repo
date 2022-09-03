def translator(phrase):
    translation = ""
    for alphabet in phrase:
        if alphabet in "AEIOUaeiou":
            translation = translation  +"g"
        else :
            translation = translation+ alphabet
    print(translation)
phrase = input("enter a phrase:")
translator(phrase)
try:
    number = int(input("enter a no: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Devide by zero")
