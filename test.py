import re

# Your text
text = """I have a text and Inside it this [
{'subject':'Thomas Jeffrey Hanks', 'relationship':'was born on', 'object':'July 9, 1956'},
{'subject':'Thomas Jeffrey Hanks', 'relationship':'is a', 'object':'American actor'},
{'subject':'Thomas Jeffrey Hanks', 'relationship':'is a', 'object':'filmmaker'}
] how can i extract just the text inside """

# Regular expression to match text within brackets
matches = re.findall(r'\[.*?\]', text, re.DOTALL)

# Get the content inside the first match (assuming there’s only one set of brackets)
if matches:
    content_inside_brackets = matches[0]
    print(content_inside_brackets)
