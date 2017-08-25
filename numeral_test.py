import pytest
import numerals

examples = [(0, 'zero'),
            (1, 'one'),
            (14, 'fourteen'),
            (18000, 'eighteen thousand'),
            (22000000000, 'twenty-two billion'),
            (40000001, 'forty million one'),
            (1000, 'one thousand'),
            (65110062, 'sixty-five million one hundred and ten thousand sixty-two'),
            (7000001000, 'seven billion one thousand'),
            (1301201300, 'one billion three hundred and one million two hundred and one thousand three hundred')]


@pytest.mark.parametrize(('num', 'word'), examples)
def test_english(num, word):
    assert numerals.english(num) == word
