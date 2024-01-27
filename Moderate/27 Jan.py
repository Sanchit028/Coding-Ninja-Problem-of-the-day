#  Best Time to Buy and Sell Stock II

from sys import stdin
def getMaximumProfit(values, n):
    hold, not_hold = -float('inf'), 0
    for i in values:            
        hold = max( hold, not_hold - i )
			
        not_hold = max( not_hold, hold + i )
    return not_hold


#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n

#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
