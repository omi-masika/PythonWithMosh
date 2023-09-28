"""Module providing a function printing python version."""


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


# def fizz_buzz(input):
#     for input in fizz_buzz:
#         if input % 3 == 0:
#             print("Fizz")
#         elif input % 5 == 0:
#             print("Buzz")
#         else:
#             print(input)


print(fizz_buzz(7))
