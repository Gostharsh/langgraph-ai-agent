

def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        raise Exception(f"Calculation Error: {e}")