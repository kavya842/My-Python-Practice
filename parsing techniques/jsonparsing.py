"""Encryption"""

data=[10,20,30,40,50,"kavya"]
import json
enc_data=json.dumps(data)
with open("file.txt","w") as fo:
    fo.write(enc_data)

"""Decryption"""
import json
with open("file.txt","r") as fo:
    res=fo.read()
    data=json.loads(res)
    print(data,type(data))
