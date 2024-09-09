import hashlib

def CrackHash(inputPass):
    try:
        with open("wordlist.txt", "r") as passFile:
            print("File opened successfully.")
            for password in passFile:
                password = password.strip()  # Remove newline characters
                encPass = password.encode("utf-8")
                digest = hashlib.md5(encPass).hexdigest()
                print(f"Checking password: {password} => MD5 Hash: {digest}")
                if digest == inputPass:
                    print("Password Found: " + password)
                    return  # Stop after finding the password
    except FileNotFoundError:
        print("Could not find file 'wordlist.txt'.")

if __name__ == '__main__':
    CrackHash("7f8a5
