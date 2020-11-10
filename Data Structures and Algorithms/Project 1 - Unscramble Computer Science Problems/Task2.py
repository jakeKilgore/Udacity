"""
Read file into texts and calls.
The text data (text.csv) has the following columns:
    sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
The call data (call.csv) has the following columns:
    calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string),
    duration of telephone call in seconds (string)
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def find_longest_time_on_phone():
    """Find the phone number that spent the longest amount of time on the phone during the month.

    Go through the calls data set and add each phone number to a dictionary, keeping track of the maximum.

    :return: The phone number that spent the longest amount of time on the phone, and the duration they spent.
    """
    numbers = {}
    longest = None
    for call in calls:
        longest = register_call(numbers, call, longest)
    return longest, numbers[longest]


def register_call(numbers, call, longest):
    """Handle adding both the caller and recipient of a call to the dictionary.

    :param numbers: A dictionary of phone numbers to time spent on the phone this month.
    :param call: The current phone call.
    :param longest: The person who has spent the most time on the phone so far.
    :return: The updated person who has spent the most time on the phone.
    """
    caller = call[0]
    recipient = call[1]
    duration = int(call[3])
    update(numbers, caller, duration)
    update(numbers, recipient, duration)
    longest = compare(caller, longest, numbers)
    longest = compare(recipient, longest, numbers)
    return longest


def compare(number1, number2, numbers):
    """The person who has spent the most time on the phone between two numbers.

    :param number1: A phone number.
    :param number2: Another phone number.
    :param numbers: A dictionary of phone numbers to time spent on the phone this month.
    :return: The person who has spent the most time on the phone between the two phone numbers.
    """
    if number1 is None:
        return number2
    if number2 is None:
        return number1
    return number1 if numbers[number1] > numbers[number2] else number2


def update(numbers, number, duration):
    """Update the value in the dictionary for the current number.

    :param numbers: A dictionary of phone numbers to time spent on the phone this month.
    :param number: The current phone number.
    :param duration: The duration of the current phone call.
    """
    time = 0 if number not in numbers else numbers[number]
    numbers[number] = time + duration


def main():
    """Find the phone number in the data set that has spent the most time on the phone."""
    number, duration = find_longest_time_on_phone()
    print(f"{number} spent the longest time, {duration} seconds, on the phone during September 2016.")


main()
