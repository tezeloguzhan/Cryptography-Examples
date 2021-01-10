from Crypto.Cipher import AES
import geocoder
import base64
from tkinter import *

key ='ry7DCOOTa3vHtI3JLuzNfoaDVJqdIXId'
iv ='Fk5mreMeFHsPHnW8'



def Encrypt_and_Decrypt():

    encryption = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = encryption.encrypt(plaintext.get())
    encoded_cipher_text = base64.b64encode(ciphertext)
    entry_text.set(encoded_cipher_text.decode())
    print("Encrypted Text:" ,encoded_cipher_text.decode())#check the encrypted text

    decryption = AES.new(key, AES.MODE_CFB, iv)
    decrypted = decryption.decrypt(base64.b64decode(encoded_cipher_text))
    entry_text_two.set(decrypted)
    print("Decrypted text", decrypted.decode()) #check the decrypted text



window=Tk()
window.title("Based on Location Data Transwer with Symmetric Cipher Algorithm")
window.geometry("600x500")

plaintext=Entry(window)
plaintext.pack()
encrypt=Button(text="Encrypt and Decrypt Your Text",command=Encrypt_and_Decrypt)
encrypt.pack()

entry_text = StringVar()
entry = Entry(window, textvariable=entry_text)
entry.pack()




entry_text_two=StringVar()
entry2 = Entry(window, textvariable=entry_text_two)
entry2.pack()



window.mainloop()