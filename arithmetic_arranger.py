def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(max_len) + "    "
        line2 += operator + operand2.rjust(max_len - 1) + "    "
        line3 += "-" * max_len + "    "
        line4 += str(eval(problem)).rjust(max_len) + "    " if show_answers else ""

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if show_answers:
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems
