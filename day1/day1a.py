# open input.txt file
with open('input.txt') as input_file:

    # for printing purposes at the end
    sum = 0
    line_idx = 0

    for line in input_file:

        line_idx += 1

        # find all the single digits in the line, written or numerical and append them to this list
        digits_in_line = []
        # list of written digits next character could be for it to be writing a digit and its index
        parsing = []

        for char in line:
            # if char is a numerical digit, append it to digits_in_line
            if char.isdigit():
                digits_in_line.append(int(char))
                
        # form a two digit number from first_number and last_number
        two_digit_number = digits_in_line[0] * 10 + digits_in_line[-1]
        print("{:<5}".format(str(line_idx)) + ": " + str(two_digit_number) + " "*5 + " <- " + str(digits_in_line))
        # increase the sum by the two digit number
        sum = sum + two_digit_number

    # print the sum of all two digit numbers
    print(" "*6 + "_______+")
    print(" "*7 + str(sum))
