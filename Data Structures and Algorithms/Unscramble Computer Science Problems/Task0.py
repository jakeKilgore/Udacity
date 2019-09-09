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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def main():
    """Output data about the first text and last call to the console.

    Time complexity: O(1).
    Space complexity: O(1).
    """
    sender, recipient, time = texts[0]
    print(f"First record of texts, {sender} texts {recipient} at time {time}.")

    caller, recipient, time, duration = calls[-1]
    print(f"Last record of calls, {caller} calls {recipient} at time {time}, lasting {duration} seconds.")


main()
