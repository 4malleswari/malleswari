time=int(input())
entry=list(map(int, input().spilt()))
exist=list(map(int, input().split()))
present=0
Total_guests=0
for i in range(time):
    present += entry[i]-exit[i]
    if Total_guests < Present:
        Total_guests = present
print(Total_guests, end=" ")
