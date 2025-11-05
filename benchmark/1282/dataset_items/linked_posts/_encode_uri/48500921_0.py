# Lets define a helper method to make it easy to use
def replacer(text, replacements):
    return reduce(
        lambda text, ptuple: text.replace(ptuple[0], ptuple[1]), 
        replacements, text
    )

if __name__ == '__main__':
    uncleaned_str = "abc&def#ghi"
    cleaned_str = replacer(uncleaned_str, [("&","\&"),("#","\#")])
    print(cleaned_str) # "abc\&def\#ghi"
