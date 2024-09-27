def main():
    """check password and print asterisks"""
    password = get_password
    print_asterisks(password)

def get_password():
    """get password from user"""
    password = input("please enter your password")

def print_asterisks(password):
    """print asterisks"""
    print("*" * len(password))

main()

