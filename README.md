# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

```python
# EXAMPLE

def get_reading_time(text):
    """Estimates reading time of the given text.

    Parameters: 
        text: a string of text or a text file
    
    Returns:
        a string containing the number of minutes, e.g. "This text will take around 25 minutes to read."

    Side effects:
        No side effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text file that takes 2 minutes or over to read
It returns a string stating the estimated time taken e.g.: "This text will take around 25 minutes to read." This is calculated by the number of words divided by 200 rounded to the nearest whole number.
"""
get_reading_time("text_long.txt") => "This text will take around 2 minutes to read."

"""
Given a text file which takes 1 minute to read
It returns "This text will take around 1 minute to read."
"""
get_reading_time("text_1_min.txt") => "This text will take around 1 minute to read."

"""
Given a text file which takes less than 1 minute to read
It returns "This text will take less than a minute to read."
"""
get_reading_time("text_short.txt") => "This text will take less than a minute to read."

"""
Given an empty text file
It returns "There is no text here to read."
"""
get_reading_time("text_empty.txt") => "There is no text here to read."

"""
Given a string of zero words
It returns "There is no text here to read."
"""
get_reading_time("text_just_spaces.txt") => "There is no text here to read."

"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!