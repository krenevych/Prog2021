try:
    assert 3 == 4, "Ну хто так порівнює?"
except AssertionError as assertion_error:
    print(assertion_error)