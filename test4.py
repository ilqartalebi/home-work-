#getting basice values for getting names

count = int(input("how many students you want to include??"))
consit_Count = count
sec_Count = 1
stu_Names = []

#inserting students name to list:

while count != 0 :

    stu_Names  += [input(f"please insert no.{sec_Count}""student names:")]
    sec_Count +=1
    count -= 1

# creating a dict for storing students scoure by theyre value

report =dict([

])

#basic value for getting scoures

count = consit_Count
sec_Count = 1
sum_Values =0
indx_Stu_Names = 0-count
value_Counter=1
user_Need = int(input("how many scoure's avg do you want to calclulate for each student?"))

#loops for calculating avg scoure for each individual

while count > 0 :
    while value_Counter < user_Need+1:
        
        sum_Values += int(input(f"value no.{value_Counter}"" "f"for student no.{sec_Count}:"))
        value_Counter +=1
    value_Counter=1
    sec_Count += 1
    count -= 1
    avg=sum_Values/user_Need
    report[stu_Names[indx_Stu_Names]]=avg
    indx_Stu_Names += 1
    avg = 0
    sum_Values = 0    

#ploting or showing ... bilmiam :)

print(report)