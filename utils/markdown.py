import re

_PATTERN = re.compile(r'(\\|\*|_|`|\[|\])')

def escape(text: str) -> str:
    """Escape telegram markdown special characters."""
    return _PATTERN.sub(lambda m: '\\' + m.group(0), text)
