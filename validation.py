def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value
            else:
                print("Please enter a whole number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")