#!/usr/bin/env python3

def is_digits(s):
    """Check if a string contains only digits."""
    return s.isdigit()

def main():
    try:
        # Ask user for input
        user_input = input("Enter a string: ")

        # Check if the string contains only digits
        if is_digits(user_input):
            print(f"The input '{user_input}' contains only digits.")
        else:
            print(f"The input '{user_input}' does not contain only digits.")
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0  # Non-zero return code indicates error

    return 1  # Success exit code

if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)


