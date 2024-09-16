# Input the current time in pm
h = int(input())

# Check if the restaurant is open (between 5 pm and 9 pm inclusive)
if 5 <= h <= 9:
    print("OPEN")
else:
    print("CLOSED")