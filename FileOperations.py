import os


def read_file_to_data(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    return list(file_data)


def write_encrypted_file(file_path, encrypted_data):
    with open(file_path, "wb") as file:
        #
        file.write(bytes(encrypted_data))


def write_decrypted_file(file_path, decrypted_data):
    with open(file_path, "wb") as file:
        
        file.write(bytes(decrypted_data))
