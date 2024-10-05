def {{ cookiecutter.function_name }}(args):
    """Compute a placeholder for the {{ cookiecutter.function_name }} function.

    Example:
        >>> compute(["1", "2", "3"])
        '1'

    """
    return max(args, key=len)
