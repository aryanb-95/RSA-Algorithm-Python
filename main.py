from termcolor import colored

from rsa.generator import generate_KeyPair
from rsa.engine import encrypt, decrypt
from rsa.storage import save_session, load_session_and_decrypt

def main():
    print("==== RSA CRYPTOSYSTEM ====")
    print("1. Encrypt a new message (note: this will erase the previous stored session)")
    print("2. Decrypt last saved message (Loads key variables from file)")
    print("3. Exit")

    choice = input("\nSelect an operational mode (1/2/3): ").strip()
    if choice == "1":
        # Stage 1: Key Generation
        print("Genrating 1024-bit primes (This takes a moment)...")
        public_key, private_key=generate_KeyPair()

        print("\n" + "+" + "-"*70 + "+")
        print("Your Private key is: ",end="")
        d_string=str(private_key[0])
        short_d = f"{d_string[:15]}.....{d_string[-15:]}"
        print(colored(f"{short_d}",'light_cyan'))
        print("\n" + "+" + "-"*70 + "+")

        # Stage 2: Encryption
        user_input = input("Enter the message: ")
        ciphertext = encrypt(user_input, public_key)

        print("\nCiphertext Generated:")
        print(colored(str(ciphertext),"green"))

        # Stage 3: File storage
        save_session("SESSION_FILE.json", ciphertext, private_key)
        print(f"Session data successfully synchronized to {colored("SESSION_FILE.json", 'magenta')}")

    elif choice == "2":
        print(f"\nReading configuration storage file from {"SESSION_FILE.json"}...")
        

        decrypted_message = load_session_and_decrypt("SESSION_FILE.json")
        
        print("\n" + "="*50)
        print(f"Decrypted Plaintext Output:\n{colored(decrypted_message, 'yellow')}")
        print("="*50)

    elif choice == "3":
        print(colored("\nExiting utility securely. Goodbye!", "red"))
    else:
        print(colored("\nInvalid option selection. Please execute again.", "red"))

if __name__ == "__main__":
    main()
