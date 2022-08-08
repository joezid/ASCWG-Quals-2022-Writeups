#Ida Python script
data=idc.GetManyBytes(0xA01E80,8208)
x=idc.GetManyBytes(0x2000C0,7615)
st=[  0x18, 0xFA, 0xCF, 0x12, 0x1D, 0x7C, 0x8F, 0xC8, 0x61, 0x4F, 
  0x03, 0x50, 0xF4, 0xCA, 0x91, 0x7F]
for i in range(7615):
    st[i%16]^=ord(x[i])
#print(st)
key=st
S = range(256)
j = 0
out = []

#KSA Phase
for i in range(256):
    j = (j + S[i] +  key[i % len(key)] ) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
with open('second_stage.bin','wb')as f:
    f.write(bytearray(out))