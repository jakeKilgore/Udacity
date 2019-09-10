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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def is_telemarketer(caller, call_recipients, texters, text_recipients):
    return caller not in call_recipients and caller not in texters and caller not in text_recipients


def format_for_output(telemarketers):
    telemarketers = list(telemarketers)
    telemarketers.sort()
    return '\n'.join(telemarketers)


def main():
    callers = set()
    call_recipients = set()
    texters = set()
    text_recipients = set()
    telemarketers = set()
    for call in calls:
        callers.add(call[0])
        call_recipients.add(call[1])
    for text in texts:
        texters.add(text[0])
        text_recipients.add(text[1])
    for caller in callers:
        if is_telemarketer(caller, call_recipients, texters, text_recipients):
            telemarketers.add(caller)
    telemarketers = format_for_output(telemarketers)
    print("These numbers could be telemarketers: ")
    print(telemarketers)


main()
