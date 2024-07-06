# 5 Subject Marks from a user
eng = float(input("Enter your marks"))
maths = float(input("Enter your marks"))
urdu = float(input("Enter your marks"))
geography = float(input("Enter your marks"))
phy = float(input("Enter your marks"))
# Total marks
totalmarks=500
# obtained marks
obtainedmarks = eng+urdu+maths+geography+phy
# calculate percentage
percentage = (obtainedmarks/totalmarks)*100

# Calculate Grades
if percentage>=90:
    print("you Secured Grade A")
elif percentage>=80 and percentage<90:
    print("you Secured Grade B")
elif percentage>=70 and percentage<80:
    print("you Secured Grade C")
elif percentage>=60 and percentage<70:
    print("you Secured Grade D")
elif percentage>=50 and percentage<60:
    print("you Secured Grade E")
else:
    ("you Failed in Exam and Secured a Grade F")

# print obtained marks & Percentage
print("==============================================================")
print("\t\t\t Mark Sheet \t\t\t ")
print("==============================================================")
print("Obtained Marks in English",eng)
print("Obtained Marks in Urdu",urdu)
print("Obtained Marks in Geography",geography)
print("Obtained Marks in Maths",maths)
print("Obtained Marks in Physics",phy)
("==============================================================")
print("Obtained Marks",obtainedmarks)
("==============================================================")
print("Percentage",percentage)
("==============================================================")



