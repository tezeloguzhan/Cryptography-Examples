from flask import Flask, jsonify
from flask import make_response
from flask import request
from Crypto.Cipher import AES
import geocoder
import base64
import json

key ='ry7DCOOTa3vHtI3JLuzNfoaDVJqdIXId'
iv ='Fk5mreMeFHsPHnW8'


mylocation = geocoder.ip('me')       
current_location = mylocation.latlng  #get current lan and lon information 
empty=' '
listToStr = empty.join([str(i) for i in current_location]) #List to String
 

encryption = AES.new(key, AES.MODE_CFB, iv)
ciphertext = encryption.encrypt(listToStr)
encoded=base64.b64encode(ciphertext) 
data=encoded.decode('ascii')
 
app = Flask(__name__)
 
@app.route('/api/location', methods=['GET'])
def get_products():
    return jsonify({'Location':data})

if __name__ == '__main__':
    app.run(debug=True)