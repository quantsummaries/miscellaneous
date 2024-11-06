def isBalanced(s):
    if len(s) == 0:
        return 'YES'
    p1 = '()'
    p2 = '[]'
    p3 = '{}'
    if (p1 not in s) and (p2 not in s) and (p3 not in s):
        return 'NO'
    else:
        for p in [p1, p2, p3]:
            s = s.replace(p, '')
        return isBalanced(s)

print(isBalanced('{[()]}'))
print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))
