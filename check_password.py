import time

real_password = "2687"


def check_password(password):
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    password_as_list = ["0", "0", "0", "0"]
    for i in range(1, 5, 1):  # digit "places" from 1 to 5 exclusive (4 digits)
        for j in range(10):  # try all possible digits - 0 to 9
            password_as_list[i - 1] = str(j)
            start = time.time()
            check_result = check_password(''.join(password_as_list))
            end = time.time()

            if check_result:
                return ''.join(password_as_list)

            if (end - start) >= (0.1 * (i + 1)):
                break

    return ''.join(password_as_list)


def someone_solution():
    itr_positions = {1, 2, 3, 4}
    itr_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    guessed_password = '0000'

    for itr_position in itr_positions:
        for itr_number in itr_numbers:
            guessed_password = guessed_password[:itr_position - 1] \
                               + str(itr_number) \
                               + guessed_password[itr_position:]
            start_time = time.time()
            res = check_password(guessed_password)
            if res:
                return guessed_password
            else:
                if time.time() - start_time >= (itr_position + 1) * 0.1:
                    break
    return guessed_password


if __name__ == "__main__":
    result = crack_password()
    print(result)
