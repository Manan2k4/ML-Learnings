import re

def tokenize(doc):
    """Extract tokens from doc.
    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer 
    or TfidfVectorizer.
    """

    return (tok.lower() for tok in re.findall(r"\w+", doc))

print(list(tokenize("This is a simple example, isn't it?")))