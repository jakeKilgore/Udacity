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
    """Check whether a number is a potential telemarketer.

    :param caller: The phone number in question.
    :param call_recipients: A set of all numbers that have received calls.
    :param texters: A set of all numbers that have sent texts.
    :param text_recipients: A set of all numbers that have received texts.
    :return: True if the number is a potential telemarketer, else false.
    """
    return caller not in call_recipients and caller not in texters and caller not in text_recipients


def format_for_output(telemarketers):
    """Format the set of potential telemarketers as a string of numbers, sorted lexicographically, and separated by
    newline characters.

    :param telemarketers: A set of potential telemarketers.
    :return: A string representing the set of telemarketers.
    """
    return '\n'.join(sorted(telemarketers))


def main():
    """Identify a list of numbers of potential telemarketers.

    Potential telemarketers are classified as numbers that make calls, but do not receive calls or send/receive texts.
    """
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
