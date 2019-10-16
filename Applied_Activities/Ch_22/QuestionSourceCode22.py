class Chapter_22():

        correct = 0

    def q1():
        #Question: If the curly E field effects charges in the same way as a non-curly E field, which equation can be used to find F caused be curly E field?

        ans1 = input("a) F = qE\n\nb) F = Vdl\n\nc) F = Emc\n\nd) F = youm\n\nanswer: ")
        if ans1 == "a" or ans1 == "F=qE" or ans1 == "F = qE":
            print("\nGreat! This is why...")
            global correct
            correct = 1
            #correct = x + 1
        else:
            print("\nTry again. This is about this....")
            correct = 0

    def q2():
        #Question: Since the curly E field is not associated with stationary charges, it is an NC field.

        ans1 = input("a) True\n\nb) False\n\nanswer: ")
        if ans1 == "a" or ans1 == "True":
            print ("\nSolid work!")
            global x
            x +=1
        else:
            print("\nIncorrect. Review...")


    def q3():
        #Question: What determines the direction of E(NC)?

        ans1 = input("a) Direction of B1\n\nb) Direction of the rate of change of $B_{1}$\n\nanswer: ")
        if ans1 == "b":
            print ("\nAmazing!")
            global x
            x +=1
        else:
            print("\nNot quite. Check this out...")


    def q4():
        #Question: If E(NC) is curling to the left, which direction is the rate of B1 chage pointing?

        ans1 = input("a) Into the page\n\nb) Out of the page\n\nc) To the ground\n\nd) To the sky\n\nanswer: ")
        if ans1 == "b" or ans1 == "Out of the page":
            print ("\nRight on!")
            global x
            x +=1
        else:
            print("\nTerrible job. Do it all over again.")


    def grade():
        global correct
        global x
        correct = float(x/4)*100
        print(correct)
