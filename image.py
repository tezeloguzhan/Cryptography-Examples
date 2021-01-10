from Crypto.Cipher import AES

key ='ry7DCOOTa3vHtI3JLuzNfoaDVJqdIXId' 
iv ='Fk5mreMeFHsPHnW8'

plain_image = open("plainimg.png",'rb') 
binary_data = plain_image.read()
plain_image.close()

encryption = AES.new(key, AES.MODE_CFB, iv)
encrypted_image = encryption.encrypt(binary_data)

encrypted_file = open("encrypted.enc", "wb")
encrypted_file.write(encrypted_image)
encrypted_file.close()


encrypted_file_read = open("encrypted.enc","rb")
encrypted_data = encrypted_file_read.read()
encrypted_file_read.close()

decryption= AES.new(key, AES.MODE_CFB, iv)
decrypted_image  = decryption.decrypt(encrypted_data)

decrypted_file = open("decrypted.jpg", "wb")
decrypted_file.write(decrypted_image)
decrypted_file.close()