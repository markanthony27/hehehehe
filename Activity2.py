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
if avg >= 75:
    print("You passed! Congrats Inamers")
else:
    print("You Failed! HEHEHE Nice Try!")

if avg >=99 & avg<=100:
    print("Your {} Average is Equivalent to A.".format(avg))
elif avg>=90 & avg<=99:
    print("Your {} Average is Equivalent to B.".format(avg))
elif avg>=80 & avg<=90:
    print("Your {} Average is Equivalent to C.".format(avg))
elif avg>=71 & avg<=80:
    print("Your {} Average is Equivalent to D.".format(avg))
elif avg>=61 & avg<=71:
    print("Your {} Average is Equivalent to E.".format(avg))
elif avg=>60:
    print("Your {} Average is Equivalent to F.".format(avg))
else:
    print("Invalid Syntax")
