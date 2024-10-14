from concrete import fhe


def encrypt_data(data):
    
    context = fhe.Context()
    context.configure(batch=True, polynomial_modulus_degree=2048, ciphertext_modulus=2048)

    
    sk, pk = context.keygen()
    
    
    encrypted_data = pk.encrypt(data)
    
    return encrypted_data, sk


def decrypt_data(encrypted_data, sk):
    
    decrypted_data = sk.decrypt(encrypted_data)
    return decrypted_data


def homomorphic_addition(encrypted_data1, encrypted_data2, sk):
    
    encrypted_sum = encrypted_data1 + encrypted_data2
    decrypted_sum = sk.decrypt(encrypted_sum)
    return decrypted_sum
