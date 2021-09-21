print("STUDENTS AVERAGE CALCULATOR")
print("     Passed Or Failed      ")
prg = int(input("Prelim    Grade  :  "))
mdg = int(input("Midterm   Grade  :  "))
sfg = int(input("SemiFinal Grade  :  "))
fg  = int(input("Final     Grade  :  "))

sum = (prg + mdg + sfg + fg)
avg = float(sum/4)
print(" ")
print("Average Grade is {}.".format((avg)))
print(" ")

if avg >=99 and avg<=100:
    print("Your {} Average is Equivalent to A.".format(avg))
    print("You Passed!")
elif avg>=90 and avg<=99:
    print("Your {} Average is Equivalent to B.".format(avg))
    print("You Passed!")
elif avg>=80 and avg<=90:
    print("Your {} Average is Equivalent to C.".format(avg))
    print("You Passed!")
elif avg>=71 and avg<=80:
    if avg>=75 and avg<=80:
        print("Your {} Average is Equivalent to D.".format(avg))
        print("You Passed!")
    else:
        print("Your {} Average is Equivalent to D.".format(avg))
        print("You Failed!")
elif avg>=61 and avg<=71:
    print("Your {} Average is Equivalent to E.".format(avg))
    print("You Failed!")
elif avg>=60:
    print("Your {} Average is Equivalent to F.".format(avg))
    print("You Failed!")
else:
    print("Invalid Syntax")