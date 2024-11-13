def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_octal(binary):
    return oct(int(binary, 2))[2:]

def binary_to_hexadecimal(binary):
    return hex(int(binary, 2))[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def octal_to_binary(octal):
    return bin(int(octal, 8))[2:]

def octal_to_hexadecimal(octal):
    return hex(int(octal, 8))[2:]

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_binary(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def hexadecimal_to_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]

def decimal_to_octal(decimal):
    return oct(int(decimal))[2:]

def decimal_to_hexadecimal(decimal):
    return hex(int(decimal))[2:]

def validate_binary(binary):
    if not set(binary).issubset({'0', '1'}):
        print("Invalid binary number. Please enter only 0s and 1s.")
        return False
    return True

def validate_octal(octal):
    if not set(octal).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
        print("Invalid octal number. Please enter only digits 0-7.")
        return False
    return True

def validate_hexadecimal(hexadecimal):
    if not set(hexadecimal.lower()).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}):
        print("Invalid hexadecimal number. Please enter only valid hexadecimal digits.")
        return False
    return True

def validate_decimal(decimal):
    try:
        int(decimal)
    except ValueError:
        print("Invalid decimal number. Please enter a valid integer.")
        return False
    return True

def main():
    print("Select Number System Format")
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    print("4. Decimal")
    
    num_system = int(input("Choose Conversion Method: "))

    if num_system == 1:
        binary = input("Enter binary number: ")
        while not validate_binary(binary):
            binary = input("Enter binary number: ")
        
        print("1. Decimal")
        print("2. Octal")
        print("3. Hexadecimal")
        
        option = int(input("Choose Conversion Method: "))
        
        if option == 1:
            print(f"Binary {binary} is converted to Decimal: {binary_to_decimal(binary)}")
        elif option == 2:
            print(f"Binary {binary} is converted to Octal: {binary_to_octal(binary)}")
        elif option == 3:
            print(f"Binary {binary} is converted to Hexadecimal: {binary_to_hexadecimal(binary)}")

    elif num_system == 2:
        octal = input("Enter octal number: ")
        while not validate_octal(octal):
            octal = input("Enter octal number: ")
        
        print("1. Decimal")
        print("2. Binary")
        print("3. Hexadecimal")
        
        option = int(input("Choose Conversion Method: "))
        
        if option == 1:
            print(f"Octal {octal} is converted to Decimal: {octal_to_decimal(octal)}")
        elif option == 2:
            print(f"Octal {octal} is converted to Binary: {octal_to_binary(octal)}")
        elif option == 3:
            print(f"Octal {octal} is converted to Hexadecimal: {octal_to_hexadecimal(octal)}")

    elif num_system == 3:
        hexadecimal = input("Enter hexadecimal number: ")
        while not validate_hexadecimal(hexadecimal):
            hexadecimal = input("Enter hexadecimal number: ")
        
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        
        option = int(input("Choose Conversion Method: "))
        
        if option == 1:
            print(f"Hexadecimal {hexadecimal} is converted to Decimal: {hexadecimal_to_decimal(hexadecimal)}")
        elif option == 2:
            print(f"Hexadecimal {hexadecimal} is converted to Binary: {hexadecimal_to_binary(hexadecimal)}")
        elif option == 3:
            print(f"Hexadecimal {hexadecimal} is converted to Octal: {hexadecimal_to_octal(hexadecimal)}")

    elif num_system == 4:
        decimal = input("Enter decimal number: ")
        while not validate_decimal(decimal):
            decimal = input("Enter decimal number: ")
        
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        
        option = int(input("Choose Conversion Method: "))
        
        if option == 1:
            print(f"Decimal {decimal} is converted to Binary: {decimal_to_binary(decimal)}")
        elif option == 2:
            print(f"Decimal {decimal} is converted to Octal: {decimal_to_octal(decimal)}")
        elif option == 3:
            print(f"Decimal {decimal} is converted to Hexadecimal: {decimal_to_hexadecimal(decimal)}")

if __name__ == "__main__":
    main()
