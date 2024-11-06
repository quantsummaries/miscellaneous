def caeserCipher(s, k):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    dictionary = {value: alphabet[(idx+k) % 26] for idx, value in enumerate(alphabet)}
    s1 = list()
    for x in s:
        lower_x = x.lower()
        if lower_x in dictionary:
            y = dictionary.get(lower_x)
            if lower_x != x:
                y = y.upper()
        else:
            y = x
        s1.append(y)
    return ''.join(s1)

print(caeserCipher(s="There's-a-starman-waiting-in-the-sky", k=3))