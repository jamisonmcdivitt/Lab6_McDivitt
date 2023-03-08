# Jamison McDivitt (Says to print name at top of file with encode function)

# Prints Menu selection
def menu():
    print('Menu\n--------')
    print('1. Encode\n2. Decode\n3. Quit\n')


# Encodes the user input string
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Decodes the user input string
def decoder(password):
    pass


def main():

    run_program = True

    while run_program:
        menu()

        user_selection = int(input('Please enter an option: '))

        if user_selection == 1:
            while True:
                user_password = str(int(input('Please enter your password to encode: ')))
                if len(user_password) != 8:
                    print('\nPassword must be 8-digits!')
                else:
                    encoded_password = encode(user_password)
                    print('Your password has been encoded and stored!')
                    break
            continue

        elif user_selection == 2:
            decoded_password = decode(user_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
            continue

        elif user_selection == 3:
            run_program = False

        else:
            print('Not a valid selection. Please select a new menu option')
            continue


if __name__ == "__main__":
    main()