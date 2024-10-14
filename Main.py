from HomomorphicEncryption import encrypt_data, decrypt_data, homomorphic_addition
from FileOperations import read_file_to_data, write_encrypted_file, write_decrypted_file


input_file = "example.txt"
encrypted_file = "encrypted_example.txt"
decrypted_file = "decrypted_example.txt"


file_data = read_file_to_data(input_file)


encrypted_data, secret_key = encrypt_data(file_data)


write_encrypted_file(encrypted_file, encrypted_data)


sum_result = homomorphic_addition(encrypted_data, encrypted_data, secret_key)
print(f"Risultato della somma omomorfa: {sum_result}")


decrypted_data = decrypt_data(encrypted_data, secret_key)


write_decrypted_file(decrypted_file, decrypted_data)

print("Cifratura e decifratura completata.")
