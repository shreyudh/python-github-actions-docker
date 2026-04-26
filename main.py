from app.calculator import Calculator


def main():
    calc = Calculator()

    x = 20
    y = 5

    print("Addition:", calc.add(x, y))
    print("Subtraction:", calc.subtract(x, y))
    print("Multiplication:", calc.multiply(x, y))
    print("Division:", calc.divide(x, y))


if __name__ == "__main__":
    main()