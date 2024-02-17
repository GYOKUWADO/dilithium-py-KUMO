from dilithium import Dilithium2
import pickle

pubkey = './pubkey.txt'
sign_file = './sign.txt'
msg = './msg.txt'

f = open(pubkey,"rb")
pk= pickle.load(f)

s = open(sign_file,"rb")
sig= pickle.load(s)

#m = open(msg, "r")
#text= bytes(m,'utf-8')
#text = eval(text)

text = bytes(input("署名したmsg.txtの文字列を入力してください。(Please enter the string in the signed msg.txt):"),'utf-8')
text = eval(text)
plain_text = text.decode('utf-8')
print(plain_text)

assert Dilithium2.verify(pk, text, sig)
print("verifed Good Sign")