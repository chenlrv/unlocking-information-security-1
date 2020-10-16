def encrypt(plaintext, k):
    cipher_text = ["0"] * len(plaintext)

    for i in range(0, len(plaintext)):
        cipher_text[i] = calculate_cipher_text_letter(plaintext[i], k[i])

    return ''.join(cipher_text)


def calculate_binary_value(letter):
    letter_ascii_value = ord(letter)
    return list(bin(letter_ascii_value)[2:])


def get_letter(binary_representation):
    decimal_value = int(binary_representation, 2)
    return chr(decimal_value)


def pad_in_zeros(binary_representation, pad_length):
    for i in range(0, pad_length):
        binary_representation.insert(0, "0")


def calculate_cipher_text_letter(plaintext_letter, key_stream_letter):
    plaintext_letter_in_binary_as_list = calculate_binary_value(plaintext_letter)
    key_stream_letter_in_binary_as_list = calculate_binary_value(key_stream_letter)

    if len(plaintext_letter_in_binary_as_list) != len(key_stream_letter_in_binary_as_list):
        number_of_missing_digits = abs(
            len(plaintext_letter_in_binary_as_list) - len(key_stream_letter_in_binary_as_list))

        pad_in_zeros(plaintext_letter_in_binary_as_list if len(plaintext_letter_in_binary_as_list) < len(
            key_stream_letter_in_binary_as_list) else key_stream_letter_in_binary_as_list, number_of_missing_digits)

    cipher_text_letter_in_binary = ["0"] * len(plaintext_letter_in_binary_as_list)
    for i in range(0, len(plaintext_letter_in_binary_as_list)):
        cipher_text_letter_in_binary[i] = str(
            int(plaintext_letter_in_binary_as_list[i]) ^ int(key_stream_letter_in_binary_as_list[i]))

    return get_letter(''.join(cipher_text_letter_in_binary))


if __name__ == "__main__":
    print(str(encrypt("1234567890", "aaaaaaaaaa")))
