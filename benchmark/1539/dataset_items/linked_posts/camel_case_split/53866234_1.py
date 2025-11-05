def split_camel(text):
    def splitter(text, char):
        if len(text) <= 1: # To avoid adding a wrong space in the beginning
            return text+char
        if char.isupper() and text[-1].islower(): # Regular Camel case
            return text + " " + char
        elif text[-1].isupper() and char.islower() and text[-2] != " ": # Detect Camel case in case of abbreviations
            return text[:-1] + " " + text[-1] + char
        else: # Do nothing part
            return text + char
    converted_text = reduce(splitter, text, "")
    return converted_text.split(" ")

split_camel("PathURLFinder")
# prints ['Path', 'URL', 'Finder']
