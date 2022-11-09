def arithmetic_arranger(inputlist, showanswer = False):
    items = []
    topnumbers = []
    bottomnumbers = []
    operators = []
    printAnswer = showanswer
    #print(inputlist)
    if len(inputlist) > 5:
        return "Error: Too many problems."
        exit(1)

    for item in inputlist:
        items = item.split(" ")
        #print(items)
        if items[1] != '+' and items[1] != '-':
            return "Error: Operator must be '+' or '-'."
            exit(1)

        if not items[0].isdigit() or not items[2].isdigit():
            return "Error: Numbers must only contain digits."
            exit(1)

        if len(items[0]) > 4 or len(items[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
            exit(1)

        #print("input is fine")
        topnumbers.append(items[0])
        operators.append(items[1])
        bottomnumbers.append(items[2])
        #print(topnumbers)
        #print(bottomnumbers)
        #print(operators)
        firstline = ''
        secondline = ''
        thirdline = ''
        answerline = ''
        i = 0
        while i < len(topnumbers):
            #print('top number is', topnumbers[i])
            #print('bottom number is', bottomnumbers[i])

            #if not first run, add 4 spaces
            if i != 0:
                firstline = firstline + (' ' * 4)
                secondline = secondline + (' ' * 4)
                thirdline = thirdline + (' ' * 4)
                answerline = answerline + (' ' * 4)

            #calculating the answer
            if operators[i] == '+':
                answer = int(topnumbers[i]) + int(bottomnumbers[i])
            else:
                answer = int(topnumbers[i]) - int(bottomnumbers[i])

            #print(answer)

            #find longer number length + 2
            length = max(len(topnumbers[i]),len(bottomnumbers[i]))+2
            #print('the length is ', length)

            #find which number needs to shift
            if len(topnumbers[i]) > len(bottomnumbers[i]):
                #top number is 2 longer
                #print('top number is longer')
                firstline = firstline + (' ' * (length - len(topnumbers[i]))) + topnumbers[i]
                secondline = secondline + operators[i] + (' ' * (length - 1 - len(bottomnumbers[i]))) + bottomnumbers[i]
                thirdline = thirdline + ('-' * length)
                answerline = answerline + (' ' * (length - len(str(answer)))) + str(answer)
            else:
                #top number is shorter
                #print('bottom number is longer')
                firstline = firstline + (' ' * (length - len(topnumbers[i]))) + topnumbers[i]
                secondline = secondline + operators[i] + ' ' + bottomnumbers[i]
                thirdline = thirdline + ('-' * length)
                answerline = answerline + (' ' * (length - len(str(answer)))) + str(answer)

            i += 1
            #find how far to shift
        #print(firstline)
        #print(secondline)
        #print(thirdline)
        #if showanswer == True:
        #    print(answerline)

    arranged_problems = firstline + '\n' + secondline + '\n' + thirdline
    if showanswer == True:
        arranged_problems = arranged_problems + '\n' + answerline

    print(arranged_problems)


#inputlist = input("Provide a list of strings:")
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 1", "2 + 2"], False)





