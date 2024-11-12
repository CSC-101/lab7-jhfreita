import sys
from convert import str_to_float
def main():
    sum = 0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number != None:
            sum += number
    print("Sum of valid numbers:", sum)

if __name__ == "__main__":
    main()

print(main())

# I could not figure out how to edit the system arguments.
# Therefore, I couldn't test this function, but the other two worked.