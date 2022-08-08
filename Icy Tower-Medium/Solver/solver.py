from Crypto.Util.number import long_to_bytes
import hashlib
import struct

rol = lambda val, r_bits, max_bits=64: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
ror = lambda val, r_bits, max_bits=64: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def R_INV(x,y,k):
    y^=x
    y=ror(y,3)
    x^=k
    x=(x-y) & 0xffffffffffffffff
    x=rol(x,8)
    return x,y,k
def R(x,y,k):
    x=ror(x,8)
    x=(x+y) & 0xffffffffffffffff
    x^=k
    y=rol(y,3)
    y^=x
    return x,y,k
def decrypt(enc,k):
    y=enc[0]
    x=enc[1]
    b=k[0]
    a=k[1]

    for i in range(31):
        a,b,i=R(a,b,i)
    for i in range(30,-1,-1):
        x,y,b=R_INV(x,y,b)
        a,b,i=R_INV(a,b,i)
    x,y,b=R_INV(x,y,b)
    return y,x

with open('data.txt.RET2','rb')as f:
    enc_b=f.read()
enc_sh=[struct.unpack("<Q",enc_b[i:i+8])[0]for i in range(0,1024,8)]
enc=[0]*128

for i in range(0,128):
    enc[i]=enc_sh[i]
k=[0x17de14e92acd03fa,0x23c207ea259b55bf]
cou=0
for i in range(0,len(enc),2):
    pl=decrypt(enc[i:i+2],k)

    for i in pl:
        print(long_to_bytes(i).decode(),end='')
