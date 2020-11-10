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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count_unique_numbers():
    """Count the unique phone numbers in the texts and calls data sets.

    Search through the list of calls and texts, keeping a set of visited numbers and counting each time a number is
    added to the set.

    :return: The number of unique numbers in the data sets.
    """
    numbers = set()
    for entry in texts:
        numbers.add(entry[0])
        numbers.add(entry[1])
    for entry in calls:
        numbers.add(entry[0])
        numbers.add(entry[1])
    return len(numbers)


def main():
    """Determine the number of unique telephone numbers in the data set and output it to the console."""
    print(f"There are {count_unique_numbers()} different telephone numbers in the records.")


main()
