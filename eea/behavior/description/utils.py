""" Utilities
"""


def truncate(text, length=300, orphans=10, suffix=".", end=".", cut=True, **kwargs):
    """
    Truncate text by the number of characters without cutting words at
    the end.

    Keyword arguments:
    text -- text to truncate
    length -- maximum length of the output text
    orphans -- the number of trailing chars not to cut
    end -- sentence end char, usually "." If provided try to return only
    complete sentences

    """

    if isinstance(text, str):
        text = text.decode("utf-8")

    text = " ".join(word for word in text.split() if word)
    if len(text) <= length + orphans:
        return text

    if end:
        res = []
        for chunk in text.split(end):
            if len(".".join(res) + "." + chunk) <= (length + orphans):
                res.append(chunk)
                continue
            else:
                break

        if res:
            length = len(res)
            res = end.join(res)
            if res[-1] not in [".", "!", "?"] and length > 1:
                res += suffix
            return res

    if cut:
        return " ".join(text[: length + 1].split()[:-1]) + suffix
    return ""
