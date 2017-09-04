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


# -----------------
# deutsch


einer = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zw\xf6lf',
         'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzechn', 'neunzehn']
zehner = [False, False, 'zwanzig', 'drei\xdfig', 'vierzig', 'f\xfcnfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']
endungen = ['', 'tausend', ' Millionen', ' Milliarden', ' Billionen', ' Billiarden', ' Trillionen', ' Trilliarden']
endungeneinzahl = ['', 'tausend', ' Million', ' Milliarde', ' Billion', ' Billiarde', ' Trillion', ' Trilliarde']


def de1start(zahl):
    return einer[zahl]


def de1ende(zahl):
    if zahl == 1:
        return 'eins'
    return einer[zahl]


def de2(zahl):
    if zahl < 20:
        return de1ende(zahl)
    ze, ei = divmod(zahl, 10)
    if ei == 0:
        return zehner[ze]
    return de1start(ei) + "und" + zehner[ze]


def de3(zahl):
    if zahl < 100:
        return de2(zahl)
    hunderterst, rest = divmod(zahl, 100)
    if rest == 0:
        return de1start(hunderterst) + "hundert"
    return de1start(hunderterst) + "hundertund" + de2(rest)


def formatieren(zahlwort: str, stufe):
    if not zahlwort:
        return ''
    if stufe == 0:
        return zahlwort + endungen[stufe]
    if stufe > 0 and zahlwort.endswith('eins'):
        zahlwort = zahlwort[:-1]  # End-s entfernen: eins --> ein
        if stufe == 1:  # ...eintausend
            return ' ' + zahlwort + 'tausend'
        zahlwort += 'e'  # ein --> eine
        return ' ' + zahlwort + endungeneinzahl[stufe]
    return ' ' + zahlwort + endungen[stufe]


def deutsch(zahl):
    if zahl == 0:
        return 'null'
    wort = ""
    for stufe in itertools.count():
        zahl, rest = divmod(zahl, 1000)
        wort = formatieren(de3(rest), stufe) + wort
        if zahl == 0:
            return wort.strip()
