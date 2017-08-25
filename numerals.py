import itertools

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = [False, False, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
endings = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']


def en1(number):
    return ones[number]


def en2(number):
    if number < 20:
        return en1(number)
    ten, one = divmod(number, 10)
    if one == 0:
        return tens[ten]
    return tens[ten] + "-" + en1(one)


def en3(number):
    if number < 100:
        return en2(number)
    hundred, rest = divmod(number, 100)
    if rest == 0:
        return en1(hundred) + " hundred"
    return en1(hundred) + " hundred and " + en2(rest)


def format_num(numberword, step):
    if numberword:
        return ' ' + numberword + ' ' + endings[step]
    return ''


def english(number):
    """Return the English numeral for the integer input."""
    if number == 0:
        return 'zero'
    word = ''
    for step in itertools.count():
        number, rest = divmod(number, 1000)
        word = format_num(en3(rest), step) + word
        if number == 0:
            return word.strip()
