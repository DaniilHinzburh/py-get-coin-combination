from app.main import get_coin_combination


def test_get_coin_combination_check_penny():
    assert get_coin_combination(1)[0] == 1


def test_get_coin_combination_check_nickel():
    assert get_coin_combination(5)[1] == 1


def test_get_coin_combination_check_dime():
    assert get_coin_combination(10)[2] == 1


def test_get_coin_combination_check_quarters():
    assert get_coin_combination(25)[3] == 1


def test_get_coin_combination_check_all():
    assert get_coin_combination(41) == [1, 1, 1, 1]
