from dilithium import Dilithium2
import pickle

text = str(input("署名する文字列を入力してください。(IN THE SIGN TO MSG):"))
text = text.encode('utf-8')
#print(text)

seckey = './seckey.txt'
msg = './msg.txt'
sign_file = './sign.txt'

f = open(seckey,"rb")
sk= pickle.load(f)

with open(msg, 'w') as f:
 print(text, file=f)

print("Generated to msg.txt")

sig = Dilithium2.sign(sk, text)

#print(sig)

in_the_sig_file = open(sign_file, 'wb')
pickle.dump(sig, in_the_sig_file)
print("Generated to sign.txt")

#test = str("XXX")
#test = test.encode('utf-8')