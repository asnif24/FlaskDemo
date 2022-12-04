def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")
    
    return dividend/divisor

grades = []

try:
    average = divide(sum(grades)/len(grades))
except ZeroDivisionError as e: # execute when error occurs
    print("There are no grades yet in your list.")
else:  # execute when no error occurs, just let code in try not too long
    print(f"The average grade is {average}")
finally: # always execute
    print("Thank you!")

