def arithmetic_arranger(problems, show_answers=False):
    """
    Arrange and format up to five arithmetic problems vertically.

    Only addition and subtraction are allowed. Returns the problems
    properly spaced and aligned. If show_answers is True, the results
    are displayed below each problem.

    Returns an error message string for invalid input.
    """
    PROBLEMS_LIMIT = 5
    MAX_DIGITS_WIDTH = 4

    # Step 1: Error Handling

    # Return an error if there are too many problems
    if len(problems) > PROBLEMS_LIMIT:
        return 'Error: Too many problems.'

    # Create an empty list to store inner lists containing each problem
    pre_output = []
    for cal in problems:
        # Using the space as a separator, separate the strings of each problem
        # and add them to a new list
        new_list = cal.split(" ")

        # Return error message if multiplication and/or division as operator
        if new_list[1] == "*" or new_list[1] == "/":
            return "Error: Operator must be '+' or '-'."

        # Return error message if both numbers are not digits
        if not new_list[0].isdigit() or not new_list[2].isdigit(): 
            return 'Error: Numbers must only contain digits.'

        # Return error message if each number is greater the max digits width   
        if len(new_list[0]) > MAX_DIGITS_WIDTH or \
        len(new_list[2]) > MAX_DIGITS_WIDTH:
            return 'Error: Numbers cannot be more than four digits.'

        # Append the new list to the outer list
        pre_output.append(new_list) 


    # Step 2: Put the string input into another list of lists to calculate 
    # the result of the problems and add the required spaces and dashes

    # Create a list to store the data to be processed 
    p_list = []
    for i in pre_output:
        # Calculate the result of each problem
        res = int(i[0]) + int(i[2])
        if i[1] == '-':
            res = int(i[0]) - int(i[2])
        i.append(str(res)) 

        # Now is a good time to handle padding for each element

        # Calculate the max length of the digits.
        # (+1 takes in consideration the extra space 
        # between the +/- sign and the digits)
        i_max_len = max(len(i[0]),len(i[2])) + 1

        # Now use the above information to construct the final problem:

        # Use the max length to calculate how many leading spaces for the numerator
        element_1 = (i_max_len - len(i[0])) * " " + i[0]
        # The second element takes in consideration the +/- sign and the denominator
        element_2 = i[1] + " " * (i_max_len-len(i[2])) + i[2]
        # The third element adds the dash line 
        element_3 = (i_max_len + 1) * '-'
        # The fourth element handles the result
        element_4 = (i_max_len - len(i[3])) * " " + i[3]

        # Display the result only if required by the user
        if show_answers == True:
            final = [element_1, element_2, element_3, element_4]
        else:
            final = [element_1, element_2, element_3]

        # Append the final lists to p_list
        p_list.append(final)

    # Step 3: Now in order to display the correct output, you need to
    # transpose the list of lists (matrix) created in the previous step

    # Compute the length of the rows and columns of the matrix
    rows = len(p_list[0])
    cols = len(p_list)

    # Build transposed matrix using list comprehension
    output = [[p_list[j][i] for j in range(cols)] for i in range(rows)]

    # Step 4: Right-align the output and add spaces between each problem

    # Compute the maximum width for each column across all rows
    # (using list comprehension + generator expression)
    widths = [max(len(row[i]) for row in output) for i in range(len(output[0]))]

    # Create a new list to store the final formatted strings
    final_output = []

    for row in output:
        # Right align the elements of each row using list comprehension
        aligned_row = [row[i].rjust(widths[i]) for i in range(len(row))]
        # When joining the strings to display the output, 
        # add 4 spaces between each problem
        final_output.append("    ".join(aligned_row))

    # Final Step: Return the formatted output
    return "\n".join(final_output)    

# Example usage / Basic tests
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')