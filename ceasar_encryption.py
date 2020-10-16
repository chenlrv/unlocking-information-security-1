alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    ciphertext = ''
    for letter in plaintext:
        letter_index = find_letter_index_in_alphabet(letter)
        encrypted_letter_index = (letter_index + k) % 26
        ciphertext = ''.join([ciphertext, alphabet[encrypted_letter_index]])
    return ciphertext


# older implementation
# def encrypt(plaintext, k):
#    for i in range(0, len(plaintext)):
#        letter = plaintext[i]
#        encrypt_index = (find_letter_index_in_alphabet(letter) - k) % 26
#        encrypted_char = alphabet[encrypt_index]
#       plaintext = plaintext[:i] + encrypted_char + plaintext[i + 1:]
#
# print(plaintext)


def find_letter_index_in_alphabet(letter):
    return ord(letter) - ord('a')


if __name__ == "__main__":
    print(encrypt('hello', 3))
