"""Knuth-Morris-Pratt string searching algorithm."""


def find_all_occurrences(text: str, pattern: str) -> list[int]:
    """Return every starting index where pattern occurs in text.

    Overlapping matches are included. An empty pattern is rejected because
    there is no useful single search position for this API.
    """
    if pattern == "":
        raise ValueError("pattern must not be empty")

    if len(pattern) > len(text):
        return []

    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            i += 1

    matches: list[int] = []
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                matches.append(text_index - pattern_index)
                pattern_index = lps[pattern_index - 1]
        elif pattern_index:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

    return matches
