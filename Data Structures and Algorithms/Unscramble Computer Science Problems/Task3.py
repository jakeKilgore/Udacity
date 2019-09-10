"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def from_bangalore(number):
    return number[0:5] == '(080)'


def add_area_code(area_codes, number):
    if number[0] == '(':
        area_codes.add(number[1:number.find(')')])
    if number[0:4] == '140':
        area_codes.add('140')
    if number.find(' ') >= 0:
        area_codes.add(number[0:4])


def format_for_output(area_codes):
    area_codes = list(area_codes)
    area_codes.sort()
    return '\n'.join(area_codes)


def main():
    calls_from_bangalore = 0
    calls_to_bangalore = 0
    area_codes = set()
    for call in calls:
        caller = call[0]
        recipient = call[1]
        if not from_bangalore(caller):
            continue
        calls_from_bangalore += 1
        if from_bangalore(recipient):
            calls_to_bangalore += 1
        add_area_code(area_codes, recipient)
    area_codes = format_for_output(area_codes)
    print(f"The numbers called by people in Bangalore have codes:")
    print(area_codes)
    percentage = (100 * calls_to_bangalore / calls_from_bangalore).__round__(2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


main()
