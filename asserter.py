from logger import Logger
import pytest

def assert_true(value, message):
    result = value is True
    assert result, message
    Logger.log_assertion(expression=message, result=result)

def assert_equal(value, reference, entity_name, compare_types=False):
    if compare_types:
        result = value == reference
    else:
        result = str(value) == str(reference)
    assert result, f'{entity_name} has expected value'
    Logger.log_assertion(
        expression=f'{entity_name} actual value [{value}] is equal to expected value [{reference}]',
        result=result
    )
