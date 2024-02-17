from dilithium import Dilithium2
import pickle

pubkey = './pubkey.txt.'
seckey = './seckey.txt.'

pk, sk = Dilithium2.keygen()

f_pub = open(pubkey, 'wb')
pickle.dump(pk, f_pub)
print("Generated to pubkey.txt")

f_sec = open(seckey, 'wb')
pickle.dump(sk, f_sec)
print("Generated to seckey.txt")