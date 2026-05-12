def repeated_letter(s):
    vistos = ""
    for char in s:
        if char in vistos:
            return char  # primeira letra repetida
        vistos += char
    return None
