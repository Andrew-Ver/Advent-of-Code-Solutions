import re
from collections import Counter

bracket = r'(\[|\])'
two_numbers = r'\[\d+,\d+\]'

test = '[[[[[9,8],1],2],3],4]'

def reduce_number(expression: str) -> str:
    #explosion
    for match in re.finditer(two_numbers, expression):
        brackets_ahead = Counter(expression[1:match.start()+1])
        if (brackets_ahead['['] >= 4 and ']' not in brackets_ahead or brackets_ahead['['] - brackets_ahead[']'] >= 4):
            number_before, number_after = re.search(r'\d+', expression[1:match.start()]), re.search(r'\d+', expression[match.end()+1:-1])
            expression = expression[:match.start()] + expression[match.end():]

    return expression

print(reduce_number(test))