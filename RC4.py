"""
"""
i = 0
def BreakingWep(key,i):
    counter = [0] * 256
    for M in Messages:
        Iv = M[0]
        if Iv[0] == i+3 and Iv[1] == 255:
            S = list(range(256))
            j = 0
            # key scheduling #
            RC4_KEY = Iv + key
            J = KSA(RC4_KEY,S,i+3)
            if S[0] == i+3 and S[1] == 0:
                Y = int(M[1][0]) ^ int('0xAA',16)
                for m in S: # Chiking the index of S[m] using Y #
                    if S[m] == Y:
                        k = (m - J - S[i+3]) % 256
                        counter[k] = counter[k] + 1
                        break
    if(i < 5): # Rec Stop #
       i = i+1 
       candidate = counter.index(max(counter)) # Sorting Count list from min to max #
       key.append(candidate)
       BreakingWep(key,i)
    else:
        print("The Key is: ", end = ' ')
        for KEY in range(len(key)):
            """str(key[KEY]).upper()"""
            print(hex(key[KEY]).replace('0x',' '), end = ' ')
        return

# key scheduling #
def KSA(key,S,i):
    j=0
    for a in range(i):
        j = (j + S[a] + int(key[a])) % 256
        S[a],S[j] = S[j],S[a]
    return j
           
"""
Pushing Each message into a List each list contains two lists
one for the IV and the another list for C, Putting all the list
in one big list:
[[v1,v2,v3,c1,c2,c3,c4],[[..][...]],...]
"""
f = open('wep.out','rb')
f = f.read()

Messages = [hex(i) for i in f]
temp = []
IV = []
C = []
I = 0
for M in Messages:  
    if I >= 0 and I <= 2:
        IV.append(int(M,16)) # Pushing vi to IV List #
        I = I + 1
    else:
        C.append(int(M,16)) # Pushing Ci to C list #
        I = I +1
        if I == 7:
            tmp = list()
            tmp.append(IV),tmp.append(C)
            temp.append(tmp)
            tmp, IV, C = [], [] ,[]
            I = 0
Messages = temp
        

BreakingWep([],0)
