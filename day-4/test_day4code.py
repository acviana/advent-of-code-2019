from day4code import(
    password_check
)


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
    assert password_check(112233, version=2) is True
    assert password_check(112333, version=2) is True
    assert password_check(111222, version=2) is False
