# Completed Nov 2020
# Recursion problems of varying difficulties

# Problem 1
def power(x,n):
    '''
    Recursively compute x^n, assuming n is a non-negative integer
    '''
    if n == 0:
        return 1
    return x * power(x,n-1)

# Problem 2 - 
def interleave(L1, L2):
    '''
    Combine L1 and L2, inserting them one element at a time
    Example: interleave([1,2,3],[4,5,6]) returns [1,4,2,5,3,6]
    '''
    if len(L1) == 0:
        return []
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

# Problem 3
def reverse_rec(L):
    '''
    Reverse list L recursively
    '''
    list = []
    if len(L) == 0:
        return L

    list.append(L[-1])
    list.extend(reverse_rec(L[:-1]))
    return list

# Problem 4
def zigzag(L): #[0,1,2,3]
    '''
    Print L in a zig-zag pattern
    Example: zigzag([0,1,2,3,4,5,6]) should print 3,2,4,1,5,0,6
    '''
    # L1: from beginning to mid-1
    # L2: from mid to end
    if len(L) % 2 != 0:
        L1 = L[:len(L)//2]
        L2 = L[len(L)//2+1:]
        print(L[len(L)//2],end=" ")
    else:
        L1 = L[:len(L)//2]
        L2 = L[len(L)//2:]
    if len(L1) == 0:
        return
    print(L1[-1], L2[0],end=" ")
    zigzag(L1[:-1] + L2[1:]) # not including what's printed
    print()

L = [1,2,3,4,5]
zigzag([1,2,3,4,5])

# Problem 5
def is_balanced(s):
    '''
    Checks to see if a string s has balanced parentheses
    Return True iff the parentheses are balanced
    '''
    if s.find("(") == -1 and s.find(")") == -1:
        return True

    if s.find(")") < s.find("("):
        return False

    loc_left = s.find("(")
    loc_right = s.find(")")
    if s.find("(") != -1 and s[s.find("("):].find(")") != -1 :
        str = s[:loc_left]+s[loc_left+1:loc_right] + s[loc_right+1:]
        print(str)

        return is_balanced(str)
    return False

print(is_balanced("(()()))((())")) # False