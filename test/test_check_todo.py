from lib.check_todo import *
"""
Given a text with '#TODO'
It returns True
"""


def test_given_text_todo():
    result = contains_todo("#TODO finish the report")
    assert result == True


"""
Given a text without '#TODO'
It returns False
"""


def test_given_text_no_todo():
    result = contains_todo("Complete the assignment")
    assert result == False


"""
Given an empty string
It returns False
"""


def test_empty_string():
    result = contains_todo("")
    assert result == False


"""
Given a text with lowercase '#todo'
It returns False
"""


def test_lowercase_string():

    result = contains_todo("#todo this should not be case sensitive")
    assert result == False


"""
Given a text with '#TODO' in the middle
It returns True
"""


def test_todo_in_the_middle():
    result = contains_todo("Remember to #TODO check the results")
    assert result == True


"""
Given a text with multiple '#TODO'
It returns True
"""


def test_multiple_todo():

    result = contains_todo("#TODO update docs, #TODO refactor code")
    assert result == True


"""
given a text with TODO with out no #
returns False
"""


def test_no_hash_in_todo():

    result = contains_todo("TODO update docs, TODO refactor code")
    assert result == False
