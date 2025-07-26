def spaced_word_regex(word):
    return r'\s*'.join(f"[{c.lower()}{c.upper()}]" for c in word)