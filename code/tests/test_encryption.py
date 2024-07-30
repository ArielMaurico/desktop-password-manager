import pytest
from src.encryption.encryption import encrypt_password, decrypt_password

def test_encrypt_password():
    # Ejemplo de prueba para encriptar una contraseña
    password = "test_password"
    encrypted_password = encrypt_password(password)
    
    assert encrypted_password != password

def test_decrypt_password():
    # Prueba para verificar que la contraseña desencriptada es igual a la original
    password = "test_password"
    encrypted_password = encrypt_password(password)
    decrypted_password = decrypt_password(encrypted_password)
    
    assert decrypted_password == password

def test_incorrect_password():
    # Prueba para verificar que una contraseña incorrecta no pasa la verificación
    password = "test_password"
    incorrect_password = "wrong_password"
    encrypted_password = encrypt_password(password)
    
    # Intentamos desencriptar usando la contraseña incorrecta
    decrypted_password = decrypt_password(encrypted_password)
    
    assert decrypted_password != incorrect_password
