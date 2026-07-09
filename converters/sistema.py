def decimal_binario(n):
    return bin(int(n))[2:]

def decimal_hexadecimal(n):
    return hex(int(n))[2:].upper()

def decimal_octal(n):
    return oct(int(n))[2:]

def binario_decimal(n):
    return int(str(n), 2)

def hexadecimal_decimal(n):
    return int(str(n), 16)

def octal_decimal(n):
    return int(str(n), 8)