from collections import Counter

most_common_english_letters = {"e", "t", "a", "o", "i", "n"}


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def update_most_common_letter(letter, occurrence, most_common_letters):
    letter_information = {"letter": letter, "occurrence": occurrence}

    if not most_common_letters:
        most_common_letters[0] = letter_information
    else:
        if occurrence >= most_common_letters[0]["occurrence"]:
            if len(most_common_letters) < 3:
                for i in range(0, len(most_common_letters)):
                    most_common_letters[len(most_common_letters) - i] = most_common_letters[
                        len(most_common_letters) - i - 1]
                most_common_letters[0] = letter_information
            else:
                most_common_letters[2] = most_common_letters[1]
                most_common_letters[1] = most_common_letters[0]
                most_common_letters[0] = letter_information

        elif occurrence >= most_common_letters[1]["occurrence"]:
            if len(most_common_letters) < 3:
                most_common_letters[2] = most_common_letters[1]
                most_common_letters[1] = letter_information
            else:
                most_common_letters[2] = most_common_letters[1]
                most_common_letters[1] = letter_information

        elif occurrence >= most_common_letters[2]["occurrence"]:
            most_common_letters[3] = letter_information


def calc_3_most_common_letters(s):
    letters_occurrences = {}

    # 0 is max, 1 is second, 2 is third
    # member in list is a dict in the following format: {"letter": "a", "occurrence": 2}
    most_common_letters = [{}] * 3

    for letter in s:
        if letter in letters_occurrences:
            letters_occurrences[letter] += 1
        else:
            letters_occurrences[letter] = 1

        occurrence = letters_occurrences[letter]
        update_most_common_letter(letter, occurrence, most_common_letters)

    return most_common_letters


def is_english(s):
    if not is_ascii(s):
        return False

    most_common_letters_in_s = calc_3_most_common_letters(s)

    most_common_letters_set = {}
    for letter_dict in most_common_letters_in_s:
        most_common_letters_set.update(letter_dict.letter)

    return most_common_letters_set in most_common_english_letters


if __name__ == "__main__":
    print(str(is_english("hello how are you yeah i feel good")))
