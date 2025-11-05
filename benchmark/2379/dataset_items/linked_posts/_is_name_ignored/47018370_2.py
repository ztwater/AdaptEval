def delta(*numbers):
    try:
        return max(numbers) - min(numbers)
    except TypeError:
        raise ValueError("delta should only be called with numerical arguments") from None
    except ValueError:
        raise ValueError("delta should be called with at least one numerical argument") from None
