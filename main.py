from arithmetic_arranger import arithmetic_arranger

# Example usage
problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

# Display problems without answers
print(arithmetic_arranger(problems1))

# Display problems with answers
print(arithmetic_arranger(problems2, True))
