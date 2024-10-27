import re
from sympy import sympify  # Make sure to have sympy installed
 
def handle_math_query(query):
    try:
        expression = re.search(r'([\d+\-*/\(\) ]+)', query).group(0)
        result = sympify(expression)  # Safe math evaluation
        return f"The answer is {result}."
    except Exception as e:
        return "I'm sorry, I don't understand the math query."
