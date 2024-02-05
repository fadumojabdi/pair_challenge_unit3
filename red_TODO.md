# {{PROBLEM}} Pair Challenge



## 1. Describe the Problem

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string '# TODO'

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def contains_todo(text):
    """Checks if the text contains the string '#TODO'

    Parameters:
        text: a string to check for the presence of '#TODO'

    Returns:
        True if the text contains '#TODO'; otherwise, False

    Side effects:
        This function doesn't modify the input text or have any other side-effects
    """
    pass  # Test-driving means not writing any code here yet.



```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a text with '#TODO'
It returns True
"""
contains_todo("#TODO finish the report") => True

"""
Given a text without '#TODO'
It returns False
"""
contains_todo("Complete the assignment") => False

"""
Given an empty string
It returns False
"""
contains_todo("") => False

"""
Given a text with lowercase '#todo'
It returns False
"""
contains_todo("#todo this should not be case sensitive") => False

"""
Given a text with '#TODO' in the middle
It returns True
"""
contains_todo("Remember to #TODO check the results") => True

"""
Given a text with multiple '#TODO'
It returns True
"""
contains_todo("#TODO update docs, #TODO refactor code") => True

"""
given a text with TODO with out no #
returns False
"""
contains_todo("TODO update docs, TODO refactor code")

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE




#  the function is in a file named lib/check_todo.py

from lib.check_todo import contains_todo

def test_contains_todo_with_todo():
    assert contains_todo("#TODO finish the report") is True

def test_contains_todo_without_todo():
    assert contains_todo("Complete the assignment") is False

def test_contains_todo_empty_string():
    assert contains_todo("") is False

def test_contains_todo_lowercase_todo():
    assert contains_todo("#todo this should not be case sensitive") is False

def test_contains_todo_todo_in_middle():
    assert contains_todo("Remember to #TODO check the results") is True

def test_contains_todo_multiple_todos():
    assert contains_todo("#TODO update docs, #TODO refactor code") is True



Ensure all test function names are unique, otherwise pytest will ignore them!
