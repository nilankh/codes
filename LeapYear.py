x=int(input("ENTER A YEAR:"))
result="LEAP YEAR" if x%400==0 else "LEAP YEAR" if x%4==0 and x%100!=0 else "NOT A LEAP YEAR"
print(result)
