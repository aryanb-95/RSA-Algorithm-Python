import json

def save_session(filename, ciphertext, private_key):
    d, n = private_key
    session_data = {
        "ciphertext": ciphertext,
        "private-key":d,
        "modulus": n
    }
    with open(filename, 'w') as file:
        json.dump(session_data,file,indent=4)

def load_session_and_decrypt(filename):
    from rsa.engine import rsa_int_to_input
    try:
        with open(filename, "r") as file:
            data= json.load(file)
        
        m = pow(data['ciphertext'],data["private-key"], data["modulus"])
        return rsa_int_to_input(m)
    except FileNotFoundError:
        return "No saved session file found!"
