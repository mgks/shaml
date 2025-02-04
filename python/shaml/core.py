# shaml/python/shaml/core.py

class ShamelessError(Exception):
    def __init__(self, message, original_value):
        self.message = message
        self.original_value = original_value

    def __bool__(self):
        return False

    def __str__(self):
        return f"Shameless Error: {self.message} with original value {self.original_value}"

    def __repr__(self):
        return f"<ShamelessError: {self.message} with original value {self.original_value}>"


def sl(value, debug=False):
    """
    Attempts to convert the input value to a more appropriate type.

    Args:
        value: The value to process.
        debug: If True, raise detailed error on failure.

    Returns:
        The converted value, or the original value if no conversion is possible.
    """

    if isinstance(value, (int, float, complex, bool)):
        return value  # Already a numeric or boolean
    elif isinstance(value, str):
        # Attempt string to number conversion
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                # Attempt string to list
                if value.strip().startswith("[") and value.strip().endswith("]"):
                    try:
                        return eval(value)
                    except:
                        pass
                # Attempt string to dict
                if value.strip().startswith("{") and value.strip().endswith("}"):
                    try:
                        return eval(value)
                    except:
                        pass
                # Attempt string to bool
                if value.lower() == 'true':
                    return True
                if value.lower() == 'false':
                    return False
                # Attempt to return original string
                return value
    elif isinstance(value, (list, tuple)):
        # Attempt to convert the list or tuple item's to sl values
        try:
            return [sl(item) for item in value]
        except:
            return value
    elif isinstance(value, dict):
        # Attempt to convert the dict value to sl values
        try:
            return {key: sl(val) for key, val in value.items()}
        except:
            return value
    else:
        return value  # return original value if no conversion is possible


if __name__ == '__main__':
    # Examples of how to use it
    print(sl("123"))
    print(sl("123.45"))
    print(sl("[1, 2, '3']"))
    print(sl("{ 'name':'Alice', 'age':'30' }"))
    print(sl("True"))
    print(sl("False"))
    print(sl(123))
    print(sl(123.45))
    print(sl(True))
    print(sl(False))
    print(sl([1, 2, "3"]))
    print(sl({"name": "Alice", "age": "30"}))
    print(sl(None))
    print(sl("hello"))
    error_test = sl("error", debug=True)
    if error_test:
        print("this should not print")
    else:
        print(error_test, error_test.message, error_test.original_value)