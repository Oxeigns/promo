import re

GROUP_LINK_RE = re.compile(r"https://t.me/(?P<username>[A-Za-z0-9_]{5,32})")


def valid_group_link(link: str) -> bool:
    return bool(GROUP_LINK_RE.fullmatch(link))
