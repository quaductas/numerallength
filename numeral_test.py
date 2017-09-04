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

beispiele = [(0, 'null'),
             (1, 'eins'),
             (101000, 'einhundertundeintausend'),
             (14000, 'vierzehntausend'),
             (56, 'sechsundfünfzig'),
             (70, 'siebzig'),
             (82_175_684, 'zweiundachtzig Millionen einhundertundfünfundsiebzigtausendsechshundertundvierundachtzig'),
             (1301201300, 'eine Milliarde dreihundertundeine Million zweihundertundeintausenddreihundert'),
             (7000001000000, 'sieben Billionen eine Million')]


@pytest.mark.parametrize(('num', 'word'), examples)
def test_english(num, word):
    assert numerals.english(num) == word


@pytest.mark.parametrize(('num', 'word'), beispiele)
def test_deutsch(num, word):
    assert numerals.deutsch(num) == word
