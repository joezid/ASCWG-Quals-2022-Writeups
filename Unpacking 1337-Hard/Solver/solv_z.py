import z3
import string
import itertools
import struct
charset = string.lowercase+string.uppercase+string.digits
charset= [ord(i)for i in charset]
s = z3.Solver()
input_length=10
flag = [z3.BitVec("x{}".format(i), 32) for i in range(input_length)]


s.add(flag[1] ^ flag[0] == 0x63172806)
s.add(flag[4] ^ flag[2] == 0x5005405)
s.add(flag[8] + flag[0] == 0x91b784a9)
s.add(flag[4] & flag[0] == 0x11434340)
s.add(flag[5] ^ flag[2] == 0x5a6b5034)
s.add(flag[8] & flag[7] == 0x1a341120)
s.add(flag[3] & flag[7] == 0x11345313)
s.add(flag[1] & flag[1] == 0x34547b47)
s.add(flag[1] + flag[8] == 0x6ec8acaf)
s.add(flag[9] & flag[3] == 0x31212109)
s.add(flag[1] | flag[4] == 0x355f7f6f)
s.add(flag[8] & flag[5] == 0x2a342148)
s.add(flag[1] | flag[5] == 0x7e747b5f)
s.add(flag[4] & flag[1] == 0x30546346)
s.add(flag[8] | flag[9] == 0x7f753169)
s.add(flag[8] | flag[8] == 0x3a743168)
s.add(flag[3] + flag[9] == 0xae989488)
s.add(flag[8] ^ flag[6] == 0x51404537)
s.add(flag[9] & flag[0] == 0x55010101)
s.add(flag[3] ^ flag[2] == 0x5284034)
s.add(flag[9] + flag[8] == 0xb7955291)
s.add(flag[1] ^ flag[6] == 0x5f600f18)
s.add(flag[2] & flag[8] == 0x30543168)
s.add(flag[3] ^ flag[1] == 0x5230818)
s.add(flag[5] ^ flag[0] == 0x3977301e)
s.add(flag[7] + flag[6] == 0xca68d392)
s.add(flag[9] & flag[8] == 0x38202128)
s.add(flag[3] | flag[9] == 0x7d77737f)
s.add(flag[2] + flag[6] == 0x9f93a7ca)
s.add(flag[3] + flag[2] == 0x65d6a6ca)
s.add(flag[6] & flag[4] == 0x2114644e)
s.add(flag[8] & flag[9] == 0x38202128)
s.add(flag[1] | flag[7] == 0x7f747f77)
s.add(flag[6] | flag[5] == 0x6f34775f)
s.add(flag[2] + flag[3] == 0x65d6a6ca)
s.add(flag[8] ^ flag[2] == 0xe2b0203)
s.add(flag[6] ^ flag[9] == 0x16155576)
s.add(flag[5] ^ flag[0] == 0x3977301e)
s.add(flag[5] ^ flag[4] == 0x5f6b0431)
s.add(flag[9] ^ flag[8] == 0x47551041)
s.add(flag[2] & flag[0] == 0x14431341)
s.add(flag[1] ^ flag[2] == 0xb482c)
s.add(flag[8] ^ flag[7] == 0x65406e5b)
s.add(flag[2] + flag[3] == 0x65d6a6ca)
s.add(flag[3] | flag[9] == 0x7d77737f)
s.add(flag[3] | flag[8] == 0x3b77737f)
s.add(flag[4] ^ flag[2] == 0x5005405)
s.add(flag[7] & flag[8] == 0x1a341120)
s.add(flag[5] | flag[6] == 0x6f34775f)
s.add(flag[5] & flag[6] == 0x6a34605f)

mx=1
count=0
while count<mx or mx==0:
    count += 1

    if s.check() == z3.sat:
        #print("test")
        model = s.model()
        serial=''
        for cc in range(10):
            serial+=(struct.pack("<I",s.model()[flag[cc]].as_long()))
        print(serial)
        block = []
        for z3_decl in model:
            arg_domains = []
            for i in range(z3_decl.arity()):
                domain, arg_domain = z3_decl.domain(i), []
                for j in range(domain.num_constructors()):
                    arg_domain.append( domain.constructor(j) () )
                arg_domains.append(arg_domain)
            for args in itertools.product(*arg_domains):
                block.append(z3_decl(*args) != model.eval(z3_decl(*args)))
            s.add(z3.Or(block))
        
