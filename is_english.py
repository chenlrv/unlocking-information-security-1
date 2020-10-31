from collections import Counter

most_common_letters_number = 3
most_common_english_letters = {"e", "t", "a", "o", "i", "n"}


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def calc_letters_occurrences(s):
    letters_occurrences = {}

    for letter in s.replace(" ", ""):  # O(n)
        if letter in letters_occurrences:
            letters_occurrences[letter] += 1
        else:
            letters_occurrences[letter] = 1

    return letters_occurrences


def calc_most_common_letters(letters_occurrences, most_common_letters_amount):
    # commonness in descending order by index: 0 is max, 1 is second, 2 is third
    # every member in the list is a dict in the following format: {"letter": "a", "occurrence": 2}
    most_common_letters = []

    for letter, occurrence in letters_occurrences.items():
        if not most_common_letters:
            most_common_letters.append({"letter": letter, "occurrence": occurrence})
            continue
        else:
            if occurrence <= most_common_letters[len(most_common_letters) - 1]["occurrence"]:
                continue  # smaller than the smallest most common letter, no need to check

            for i in range(0, len(most_common_letters)):
                if occurrence >= most_common_letters[i]["occurrence"]:
                    if len(most_common_letters) < most_common_letters_amount:
                        most_common_letters.append({})
                    for j in range(len(most_common_letters) - 1, i, -1):  # moving all values to the right
                        most_common_letters[j] = most_common_letters[j - 1]
                    most_common_letters[i] = {"letter": letter, "occurrence": occurrence}
                    break

    return most_common_letters


# 2 generic solutions that works for every number of most common letters.
# Complexity: O(n*most_common_letters_number)
def calc_3_most_common_letters(s):
    letters_occurrences = calc_letters_occurrences(s)
    most_common_letters = calc_most_common_letters(letters_occurrences, most_common_letters_number)

    return list(letter_occurrence['letter'] for letter_occurrence in most_common_letters)


# Complexity: O(nlogn)
def calc_3_most_common_letters_using_max(s):
    # sorted dict of letters occurrences
    sorted_letters_occurrences = {k: v for k, v in
                                  sorted(calc_letters_occurrences(s).items(), key=lambda item: item[1], reverse=True)}
    # this would produce a sorted list and not a dict:
    # sorted(calc_letters_occurrences(s).items(), key=lambda x: x[1], reverse=True)
    most_common_letters = list(sorted_letters_occurrences.keys())[0:3]

    return most_common_letters


def is_english(s):
    if not is_ascii(s):
        return False

    most_common_letters_in_s = calc_3_most_common_letters(s)

    return all(letter in most_common_english_letters for letter in most_common_letters_in_s)


if __name__ == "__main__":
    print(str(is_english("hello nice to meet you today")))
