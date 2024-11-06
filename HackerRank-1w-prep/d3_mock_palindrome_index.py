def palindromeIndex(s):
    n = len(s)

    if n <= 1:
        return -1

    # check if the string is already palindrome
    palindrome = True
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            palindrome = False
            break
    if palindrome:
        return -1

    # check which index to remove
    for i in range(n):
        idx1 = 0
        idx2 = n - 1

        palindrome = True
        while idx1 < idx2:
            if i == idx1:
                idx1 += 1
            elif i == idx2:
                idx2 -= 1

            if s[idx1] != s[idx2]:
                palindrome = False
                break

            idx1 += 1
            idx2 -= 1

        if palindrome:
            return i
    return -1

print(palindromeIndex('aaab'))
print(palindromeIndex('baa'))
print(palindromeIndex(('aaa')))
print(palindromeIndex('quyjjdcgsvvsgcdjjyq'))
print(palindromeIndex('hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh'))
