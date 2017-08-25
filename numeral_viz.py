from csv import writer
import numerals


def get_wordlen(word: str):
    return len(word.replace(" ", ""))


def makecsv(word_function, filename, start=0, end=1001, step=1, includeword=False):
    """
    Make a CSV file containing all numbers in a given range and the corresponding length of the numeral.

    Positional arguments:
    word_function -- the function to use for creating numerals - this would be numerals.english
    filename -- the filename to output the CSV file to

    Keyword arguments:
    start, end, step -- arguments for the range in which to write the CSV file. Work just like in the built-in range() function. Defaults: start=0, end=1001, step=1
    includeword -- whether to include the actual numeral or not. default is False
    """

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = writer(csvfile, delimiter=',')
        if includeword:
            csvwriter.writerow(("number", "wordlen", "numeral"))
        else:
            csvwriter.writerow(("number", "wordlen"))
        for i in range(start, end, step):
            numeral = word_function(i)
            if includeword:
                csvwriter.writerow((i, get_wordlen(numeral), numeral))
            else:
                csvwriter.writerow((i, get_wordlen(numeral)))
