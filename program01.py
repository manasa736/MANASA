##def solveProblem(s):
##    lst=s.split()
##    return [i[::-1] for i in lst]
##
##inp=input()
##print(*solveProblem(inp))



def reverseString(s):
  ans=[i[::-1]for i in s]
  return ans

inp=input().split()
#
print(inp)
print(*reverseString(inp))
