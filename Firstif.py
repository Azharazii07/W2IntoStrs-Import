YOB = int(input("Enter Year of Birth\n"))
currentY = 2026
age = currentY - YOB
print("You are",age,"Years Old")

if(age<=13):
    print("You are Underage")
    print("You have to wait for another",14-age,"years")
else :
    print("You are 13+")
    print("Please enjoy","(crossed 13,",age-14,"years ago)")
print("TYSM for visiting")
