print("Enter your grade marks:")
a=(int(input("Enter your 1st subject grade:")))
b=(int(input("Enter your 2nd subject grade:")))
c=(int(input("Enter your 3rd subject grade:")))
d=(int(input("Enter your 4th subject grade:")))
no=4
grade=(a+b+c+d)/no

print("Enter your viva marks:")
p=(int(input("Enter your 1st sub viva marks:")))
q=(int(input("Enter your 2nd sub viva marks:")))
r=(int(input("Enter your 3rd sub viva marks:")))
s=(int(input("Enter your 4th sub viva marks:")))
num=4
viva=(p+q+r+s)/num

total=2
Average_grade=(grade+viva)/total
print("The averge grade of viva and grades are:",Average_grade)