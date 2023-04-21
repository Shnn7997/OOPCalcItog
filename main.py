import logging
from complex_number_factory import ComplexNumberFactory

# Logging setup
logging.basicConfig(filename="calculator.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Menu
print("Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square root")
print("6. Exit")

# Input from user
choice = int(input("Enter your choice: "))

# Complex number factory
cn_factory = ComplexNumberFactory()

# Addition
if choice == 1:
    a = cn_factory.create_complex_number(input("Enter first number: "))
    b = cn_factory.create_complex_number(input("Enter second number: "))
    sum = a.add(b)
    print("Sum =", sum)
    logger.info("Addition: {} + {} = {}".format(a, b, sum))

# Subtraction
elif choice == 2:
    a = cn_factory.create_complex_number(input("Enter first number: "))
    b = cn_factory.create_complex_number(input("Enter second number: "))
    diff = a.subtract(b)
    print("Difference =", diff)
    logger.info("Subtraction: {} - {} = {}".format(a, b, diff))

# Multiplication
elif choice == 3:
    a = cn_factory.create_complex_number(input("Enter first number: "))
    b = cn_factory.create_complex_number(input("Enter second number: "))
    product = a.multiply(b)
    print("Product =", product)
    logger.info("Multiplication: {} * {} = {}".format(a, b, product))

# Division
elif choice == 4:
    a = cn_factory.create_complex_number(input("Enter first number: "))
    b = cn_factory.create_complex_number(input("Enter second number: "))
    if b.is_zero():
        print("Division by zero is not allowed.")
    else:
        div = a.divide(b)
        print("Quotient =", div)
        logger.info("Division: {} / {} = {}".format(a, b, div))

# Square root
elif choice == 5:
    a = cn_factory.create_complex_number(input("Enter number: "))
    sqrt = a.square_root()
    print("Square root =", sqrt)
    logger.info("Square root: sqrt({}) = {}".format(a, sqrt))

# Exit
elif choice == 6:
    logger.info("Exiting the calculator.")
    exit()

# Invalid choice
else:
    print("Invalid choice.")
    logger.info("Invalid choice.")