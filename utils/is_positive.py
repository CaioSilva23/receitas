def is_positive(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return value > 0
