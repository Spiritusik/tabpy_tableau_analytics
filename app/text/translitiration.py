from transliterate import translit

def transliterate(value):
    result = []

    for str in value:
        try:
            transliterate_value = translit(str, 'uk', reversed=True)
            result.append(transliterate_value.upper())
        except:
            result.append(str)

    return result