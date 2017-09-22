# Dynamic Programming - Baekjoon youtube lecture
# ----------------------------------------------------------------- #
# [1] Make it to 1
# There are three operations possible to a integer.
# Use these three accordingly so that the integer becomes 1 in minimal operations.
# 1) if X is divisible by 3, then able to divide it by 3.
# 2) if X is divisible by 2, then able to divide it by 2.
# 3) Subtract by 1.

def min_three(a,b,c):
    return min(min(a,b),c)

def find_optimal(num):
    #print num
    if(num==1):
        return 0
    else:
        A = 10000007
        B = 10000007
        C = 10000007
        if(num%3==0):
            A = find_optimal(num/3)
        if(num%2==0):
            B = find_optimal(num/2)
        C = find_optimal(num-1)
        return min_three(A, B, C) + 1
    
print find_optimal(10) # 3
# ----------------------------------------------------------------- #
# [2] Make it to 1 with "memoization"
def min_three(a,b,c):
    return min(min(a,b),c)

def find_optimal(num, cache=dict()):
    cache[(1)]=0
    if num in cache:
        return cache[(num)]
    if(num==1):
        return 0
    else:
        A = 10000007
        B = 10000007
        C = 10000007
        if(num%3==0):
            A = find_optimal(num/3) + 1            
        if(num%2==0):
            B = find_optimal(num/2) + 1
        C = find_optimal(num-1) + 1
        
        cache[(num)] = min_three(A,B,C)        
        return cache[(num)]

print find_optimal(10)
# ----------------------------------------------------------------- #
# [3] 2*N tiles
# Rectangle of 2*N size is given.
# Calculate the possible number of combinations that this rectangle 
# can be filled with sub-rectangles of 1x2 and/or 2x1.
def find_tile(N):
    if(N==1):
        return 1
    elif(N==2):
        return 2
    else:
        return find_tile(N-1) + find_tile(N-2) # turns out being finonazzi sequence

print find_tile(5)
# ----------------------------------------------------------------- #
# [4] 2*N tiles2
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">find_tile2</span>(N):
    <span style="color: #008800; font-weight: bold">if</span>(N<span style="color: #333333">==</span><span style="color: #0000DD; font-weight: bold">1</span>):
        <span style="color: #008800; font-weight: bold">return</span> <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #008800; font-weight: bold">elif</span>(N<span style="color: #333333">==</span><span style="color: #0000DD; font-weight: bold">2</span>):
        <span style="color: #008800; font-weight: bold">return</span> <span style="color: #0000DD; font-weight: bold">3</span>
    <span style="color: #008800; font-weight: bold">else</span>:
        <span style="color: #008800; font-weight: bold">return</span> find_tile2(N<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>) <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">2</span><span style="color: #333333">*</span>find_tile2(N<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">2</span>)

<span style="color: #008800; font-weight: bold">print</span> find_tile2(<span style="color: #0000DD; font-weight: bold">5</span>) <span style="color: #888888">#21</span>
</pre></div>

# -----------------------------------------------------------------#
# [5] Combination of 1,2 and 3
# The possible number of combinations that an integer N can be represented as sums of 1, 2 and/or 3.
# if N=4, find_combination(N)=7 listing: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1.
def find_combination(N):
    if(N==1):
        return 1
    elif(N==2):
        return 2
    elif(N==3):
        return 4
    else:
        return find_combination(N-1) + find_combination(N-2) + find_combination(N-3)

print find_combination(4) # 7    
print find_combination(10) # 274
# ----------------------------------------------------------------- #
# [6] Selling breads
# Given N breads, find the max revenue for different price combinations.
# P[i] is revenue selling i breads. Find Max revenue selling all.

N = int(raw_input())
arr = map(int, raw_input().strip().split(' '))

def find_optimal(arr,num): # maximum cost by selling 'num' items
    
    if(num==0):
        return 0
    if(num==1):
        return arr[0]
    temp = 0
    for i in range(1,num+1): # num is 4,  i being [1, 2, 3, 4]        
        temp = max(temp,find_optimal(arr,num-i) + arr[i-1]) # opt(3)+cost(1), opt(2)+cost(2), opt(1)+cost(3)
    print "printing", arr, num, temp
    return temp    

print find_optimal(arr,N)

# -----------------------------------------------------------------#
# [7] Easy Stair Number
# It refers to a number whose digit difference is 1
# Example: 45656(N=5), 1234543456(N=10)
# Find the possible number of easy stair number whose length is N
N = int(raw_input())
def find_case(length,ending): # length=2 and ending 3
    #print length,ending
    if(ending<0 or ending>9):
        return 0
    if(length==1):
        return 1
    return find_case(length-1,ending+1) + find_case(length-1,ending-1)
#print find_case(3,1)   
count = 0
for i in range(0,10):
    count = count + find_case(N,i)
print count  
# ----------------------------------------------------------------- #
# [8] Ascending number
# It refers to a number whose digits are assending.
# Neighbor digits should assend or can be equal.
# Example: 12333345, 357, 88888888, 155555999
# Find the possible number of ascending number whose length is N
# The first digit of a number can be 0.
N = int(raw_input())
def find_case2(length,ending): # length=2 and ending 3
    #print length,ending
    result = 0
    if(ending<0 or ending>9):
        return 0
    if(length==1):
        return 1
    for i in range(0,ending+1):
        result = result + find_case2(length-1,i)
    return result
count = 0
for i in range(0,10): # i = [0, 1, 2, ~, 9]
    count = count + find_case2(N,i)
print count       
# ----------------------------------------------------------------- #
# [9] The friendly binary
# The number only consists of 0 or 1 is called binary.
# The friendly binary meets the following
# 1) The first digit is not 0.
# 2) 1 does not appear more than twice in a row. 11 can't be its subnumber
# Find the possible number of the friendly binary whose length is N.
# D[N][0] = D[N-1][0] + D[N-1][1]
# D[N][1] = D[N-1][0]
# D[N] = D[N][0] + D[N][1]  
# D[1][1] = 1, D[1][0] = 0
N = int(raw_input())
def find_case3(length,ending): # binary_friend
    #print length,ending
    if(ending==0 and length==1):
        return 0
    if(ending==1 and length==1):
        return 1
    if(ending==0):
        return find_case3(length-1,0) + find_case3(length-1,1)
    elif(ending==1):
        return find_case3(length-1,0)
    
count = 0
for i in range(0,2):
    count = count + find_case3(N,i)
    
print count    
#-----------------------------------------------------------------#
# [10] The friendly binary solving with different approach
# 이친수 - 다르게 풀기
# D[N] = N자리 이친수
# 마지막수 0 = D[N-1]
# 마지막수 1 = D[N-2]
# 그래서 D[N] = D[N-1] + D[N-2] 와우!

#-----------------------------------------------------------------#
# [11] Wine free sample
# Given N free samples of wine, find the max sample you can drink in this constraint.
# Cannot drink more than 3 samples together.
# N=6
# arr= [6 10 13 9 8 1]
# max is 6 10 13(skip), 9, 8, 1(skip) => 33
# max_drink(arr)=33
# => 33
def max_drink(arr):
    n = len(arr)
    if(n==0):
        return 0
    elif(n==1):
        return arr[0]
    elif(n==2):
        return arr[0]+arr[1]   
    else:
        return max(max(max_drink(arr[:-1]), max_drink(arr[:-2]) + arr[n-1]), max_drink(arr[:-3]) + arr[n-1] + arr[n-2])


N = int(raw_input())
arr = map(int, raw_input().strip().split(' '))
print max_drink(arr)
#-----------------------------------------------------------------#  
