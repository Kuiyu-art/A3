from kyber_py.ml_kem import ML_KEM_768
ek, dk= ML_KEM_768.keygen()

print("Alice's encapsulation key", len(ek) ,"bytes")
print("Alice's encapsulation key", len(dk) ,"bytes")

# 2. Encapsulation (sender side)
shared_secret_bob, ciphertext = ML_KEM_768.encaps(ek)

print("Ciphertext:", len(ciphertext), "bytes")
print("Sender shared secret:", shared_secret_bob.hex())

# 3. Decapsulation (receiver side)
shared_secret_alice = ML_KEM_768.decaps(dk,ciphertext)

print("Alice's shared secret:", shared_secret_alice.hex())

# Verify consistency
if shared_secret_alice == shared_secret_bob:
    print("Shared secrets match — ML-KEM demonstration completed successfully!")
else:
    print("Shared secrets do NOT match — something went wrong!")