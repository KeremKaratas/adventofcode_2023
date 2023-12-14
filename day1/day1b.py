digit_strings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

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
            else:  # not a numerical digit
                # if it's not empty, check if char matches anything in parsing word list
                if parsing:

                    # list to remove elements from parsing after loop
                    rm_list = []

                    for list_idx, (word, parse_idx) in enumerate(parsing):
                        # if character matches the next character of the parsed word
                        if word[parse_idx] == char:
                            # if char is the last character in the word
                            if parse_idx + 1 == len(word):
                                # add the digit to digits_in_line
                                digits_in_line.append(digit_strings[word])
                                # if read the full word remove it from parsing
                                rm_list.append(list_idx)
                            else:
                                # if character is not the last element
                                # but matches increment its index
                                parsing[list_idx] = [word, parse_idx + 1]
                        else:
                            # if next char doesn't match remove the word from parsing
                            rm_list.append(list_idx)

                    for idx in rm_list[::-1]:
                        del parsing[idx]

                # for each possible written digit
                # check if char matches the first character in the word
                # if so add it to parsing with index 1
                for written_digit in digit_strings:
                    if (char == written_digit[0]):
                        parsing.append([written_digit, 1])

        # form a two digit number from first_number and last_number
        two_digit_number = digits_in_line[0] * 10 + digits_in_line[-1]
        print("{:<5}".format(str(line_idx)) + ": " + str(two_digit_number) + " "*5 + " <- " + str(digits_in_line))
        # increase the sum by the two digit number
        sum = sum + two_digit_number

    # print the sum of all two digit numbers
    print(" "*6 + "_______+")
    print(" "*7 + str(sum))
