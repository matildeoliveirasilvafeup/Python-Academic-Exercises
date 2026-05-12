def camel_case(phrase):
    phrase = phrase.strip()
    result = ''
    capitalize_next = False
    first_letter = True  # nova flag para a primeira letra

    for letter in phrase:
        if not letter.isalpha():
            capitalize_next = True #"  NumberOne" fica numberone e ",!What about Now?" fica whatAboutNow
        else:
            if first_letter:
                result += letter.lower()  # primeira letra minúscula
                first_letter = False
                capitalize_next = False  # reseta a flag
            elif capitalize_next:
                result += letter.upper()
                capitalize_next = False
            else:
                result += letter.lower()
    return result
