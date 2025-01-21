import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits 
    symbols = "!@$+="

    pool = ""
    if use_upper:
        pool += upper 
    if use_lower:
        pool += lower
    if use_numbers:
        pool += numbers
    if use_symbols:
        pool += symbols

    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_lower:
        password.append(random.choice(lower))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(symbols))
    
    while len(password) < length:
        password.append(random.choice(pool))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator")

    length = int(input("How many characters do you want your password to be?: "))

    use_upper = input("Do you want to include upper case letters? Type y/n: ").lower() == "y"
    use_lower = input("Do you want to include lower case letters? Type y/n: ").lower() == "y"
    use_numbers = input("Do you want to include numbers? Type y/n: ").lower() == "y"
    use_symbols = input("Do you want to include symbols? Type y/n: ").lower() == "y"

    password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)
    print(f"\nYour random password is {password}")

main()
