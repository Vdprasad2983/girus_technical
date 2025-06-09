def evaluate(expression):
    vars = {}
    lines = expression.strip().split("\n")
    for line in lines:
        if line.startswith("let"):
            parts = line[4:].split("=")
            key, val = parts[0].strip(), eval(parts[1].strip(), {}, vars)
            vars[key] = val
        elif line.startswith("if"):
            cond = line[3:].split(":")
            if eval(cond[0].strip(), {}, vars):
                print(eval(cond[1].strip(), {}, vars))

# Test Case
input_expr = """
let x = 10
let y = 5
if x > y: x + y
"""
evaluate(input_expr)
