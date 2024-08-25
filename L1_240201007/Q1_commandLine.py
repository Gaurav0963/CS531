import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python Q1_commandLine.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
