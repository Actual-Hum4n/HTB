#!/usr/bin/python2.7
import random

#hex vars that defines the username
db = '\x6e'
lr = '\x64'
ef = '\x63'
nn = '\x61'
ty = '\x61'
gh = '\x6e'
aa = '\x61'
rr = '\x6f'
slither = aa + db + nn + ef + rr + gh + lr + ty

#arrays in hex, notice auth is not used anywhere, commenting out to make things easier to read
chars = []
keys = [0x70, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x21, 0x21]
chains = [0x74, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x74, 0x72, 0x6f, 0x6c, 0x6c]
password = [0x69, 0x74, 0x73, 0x20, 0x6e, 0x6f, 0x74, 0x20, 0x74, 0x68, 0x61, 0x74, 0x20, 0x65, 0x61, 0x73, 0x79]
#auth = [0x6b, 0x65, 0x65, 0x70, 0x20, 0x74, 0x72, 0x79, 0x69, 0x6e, 0x67]

#function that defines the lock for later encryption
lock_pick = random.randint(0, 0x3e8)
lock = lock_pick * 2
lock = lock + 10
lock = lock / 2
lock = lock - lock_pick

#turns the arrays into plaintext and prints the output
uchars = []
ukeys = []
uchains = []
upassword = []

for key in keys:
     ukeys.append(chr(key))
print('Key:'+"".join(ukeys))
for chain in chains:
     uchains.append(chr(chain))
print('Chains:'+"".join(uchains))
for passw in password:
     upassword.append(chr(passw))
print('Password:'+"".join(upassword))
print ''

#start of program
print 'The Snake Created by 3XPL017'
print 'Your number is ' + str(lock_pick)

#encrypts the key with an xor of the lock and every character in the keys array
#appends the output into chars array and prints the current char array
for key in keys:
    keys_encrypt = lock ^ key
    chars.append(keys_encrypt)
    uchars.append(chr(keys_encrypt))
print('Key Encrypt:' + "".join(uchars))


#appends the output into chars array and prints the current char array
for chain in chains:
    chains_encrypt = chain + 0xA
    chars.append(chains_encrypt)
    uchars.append(chr(chains_encrypt))
print('Chars:' + "".join(uchars))

print ''

print('Username is:' + slither)
print('Password is:' + "".join(uchars))

print 'Authentication required'
print ''
user_input = raw_input('Enter your username\n')
if user_input == slither:
    pass

else:
    print 'Wrong username try harder'
    exit()

pass_input = raw_input('Enter your password\n')
for passes in pass_input:
    for char in chars:
        if passes == str(chr(char)):
            print 'Good Job'
            break
        else:
            print 'Wrong password try harder'
            exit(0)
    break

