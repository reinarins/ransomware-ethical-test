from cryptography.fernet import Fernet
import os


def return_key():
    return open("key.key", "rb").read()


def decrypt(elements, key):
    f = Fernet(key)
    for element in elements:
        with open(element, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(element, "wb") as file:
            file.write(decrypted_data)


if __name__ == "__main__":
    path = "C:\\Users\\yukik\\OneDrive\\Escritorio\\ransomfiles"
    os.remove(path + "\\" + "readme.txt")
    elements = os.listdir(path)
    full_path = [path + "\\" + element for element in elements]

    key = return_key()
    decrypt(full_path, key)
