def validate_plan(plan):

    valid_plan = []

    math_symbols = ["+", "-", "*", "/", "%", "(", ")"]

    for step in plan:

        tool = step.get("tool", "")
        tool_input = step.get("input", "").strip()

        # ------------------
        # calculator
        # ------------------

        if tool == "calculator":

            has_digit = any(ch.isdigit() for ch in tool_input)

            has_math = any(sym in tool_input for sym in math_symbols)

            if has_digit and has_math:
                valid_plan.append(step)

        # ------------------
        # get_time
        # ------------------

        elif tool == "get_time":

            valid_plan.append(step)

        # ------------------
        # pdf_search
        # ------------------

        elif tool == "pdf_search":

            if not tool_input:
                continue

            has_math = any(sym in tool_input for sym in math_symbols)

            if not has_math:
                valid_plan.append(step)

    return valid_plan