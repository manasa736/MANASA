string='''practice problems for list comprehension in python.'''

##ans=[]
##for i in string:
##    if i  not in 'AEIOUaeiou':
##        ans.append(i)
##print(*ans)


ans=[i for i in string if i not in 'AEIOUaeiou']
print(*ans)
