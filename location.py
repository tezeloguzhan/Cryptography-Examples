from Crypto.Cipher import AES
import geocoder
import base64

key ='ry7DCOOTa3vHtI3JLuzNfoaDVJqdIXId'
iv ='Fk5mreMeFHsPHnW8'


mylocation = geocoder.ip('me')       
current_location = mylocation.latlng  #get current lan and lon information  
empty=' '
listToStr = empty.join([str(i) for i in current_location]) #List to String
 

encryption = AES.new(key, AES.MODE_CFB, iv)
ciphertext = encryption.encrypt(listToStr)
print(ciphertext) #check the encrypted text

decryption = AES.new(key, AES.MODE_CFB, iv)
plaintext = decryption.decrypt(ciphertext)
print(plaintext.decode()) #check the decrypted text