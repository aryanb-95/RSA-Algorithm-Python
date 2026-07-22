def input_to_rsa_int(user_input):
    byte_data = str(user_input).encode('utf-8')
    return int.from_bytes(byte_data, byteorder='big')

def encrypt(message, public_key:tuple[int,int]):
    e,n = public_key
    m = input_to_rsa_int(message)
    return pow(m,e,n)

def rsa_int_to_input(large_int):
    byte_length = (large_int.bit_length()+7)//8
    byte_data= large_int.to_bytes(byte_length,byteorder='big')
    return byte_data.decode('utf-8')

def decrypt(cipher_text, private_key:tuple[int,int]):
    d,n=private_key
    m = pow(cipher_text,d,n)
    return rsa_int_to_input(m)