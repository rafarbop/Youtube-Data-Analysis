from app.operations import soma


def test_soma():
    """Testing the function soma."""
    number_1 = 50
    number_2 = 20
    result_expected = number_1 + number_2
    assert soma(number_1, number_2) == result_expected
