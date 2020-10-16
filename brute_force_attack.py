alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    print(decrypt(ciphertext, 17))


brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
