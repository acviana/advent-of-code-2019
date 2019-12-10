'''
https://adventofcode.com/2019/day/4
'''


def password_check(password, version, lower_limit=100000, upper_limit=999999):
    '''
    Return True if:
        - It is a six-digit number.
        - The value is within the range given in your puzzle input.
        - Two adjacent digits are the same (like 22 in 122345).
        - Going from left to right, the digits never decrease; they
            only ever increase or stay the same (like 111123 or 135679).
    '''
    # Check limits
    if password < lower_limit or password > upper_limit:
        return False

    # Check length
    if not (password > 99999 and password < 1000000):
        return False

    string_password = str(password)

    # Check for increasing digits
    increasing_digits = True
    for digit in range(len(string_password) - 1):
        if string_password[digit] > string_password[digit + 1]:
            increasing_digits = False
    if increasing_digits is False:
        return False

    # Check for repeat digits
    if version == 1:
        repeat_digits = False
        for digit in range(len(string_password) - 1):
            if string_password[digit] == string_password[digit + 1]:
                repeat_digits = True
        if repeat_digits is False:
            return False
    elif version == 2:
        # print(f'Password is {password}')
        repeat_digits = False
        for digit in range(len(string_password) - 1):
            # print(f'Index is {digit}, value is {string_password[digit]}')
            if string_password[digit] == string_password[digit + 1]:
                # print(
                #     f'Potential match found at index {digit}, '
                #     f'value {string_password[digit]} next value value {string_password[digit + 1]}')
                try:
                    if string_password[digit] != string_password[digit + 2]:
                        repeat_digits = True
                except IndexError:
                    if string_password[digit] != string_password[digit - 1]:
                        repeat_digits = True
        if repeat_digits is False:
            return False
    else:
        raise KeyError(f'Version value of {version} is not allowed')

    return True


def test_password_check_v1():
    assert password_check(1, version=1) is False
    assert password_check(1111111, version=1) is False
    assert password_check(111111, version=1) is True
    assert password_check(223450, version=1) is False
    assert password_check(123789, version=1) is False


def test_password_check_v2():
    assert password_check(112233, version=2) is True
    assert password_check(123444, version=2) is False
    assert password_check(111122, version=2) is True


def main(lower_limit, upper_limit, version):
    return sum([
        password_check(password, version=version) for password
        in range(lower_limit, upper_limit)
    ])


if __name__ == '__main__':
    print(f'Version 1 answer is: {main(236491, 713787, version=1)}')
    print(f'Version 2 answer is: {main(236491, 713787, version=2)}')
