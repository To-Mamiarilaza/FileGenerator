
def classToCamelCase(text):
    result = text.split("_")
    capitalizedResult = [mot.capitalize() for mot in result]
    return "".join(capitalizedResult) 

def fieldToCamelCase(text):
    result = text.split("_")
    capitalizedResult = [result[0]] + [mot.capitalize() for mot in result[1:]]
    return "".join(capitalizedResult)

def capitalizeFirstLetter(text):
    if not text:
        return text  # Retourne la chaîne telle quelle si elle est vide
    return text[0].upper() + text[1:]

def toLowerFirstLetter(text):
    if not text:
        return text
    return text[0].lower() + text[1:]