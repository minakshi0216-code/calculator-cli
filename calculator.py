# This is a  calculator
#created by Minakshi
print("Welcome to  Calculator")
print("Type 'exit' to close the calculator \n")

while True:
    # ask user for input
    expression = input("Enter calculation: ")

    # if user types exit → stop the loop
    if expression.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        # calculate the answer
        answer = eval(expression)
        print("Answer:", answer)
    except:
        print("Please enter a valid math expression")