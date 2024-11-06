class Editor:
    def __init__(self):
        self.s = ''
        self.ops_stack = list()
        self.val_stack = list()

    def __str__(self):
        return self.s + ' ' + str(self.ops_stack) + ' ' + str(self.val_stack)

    def append(self, w):
        self.ops_stack.append(1)
        self.val_stack.append(w)
        self.s += w

    def delete(self, k):
        self.ops_stack.append(2)
        self.val_stack.append(self.s[-k:])
        self.s = self.s[:-k]

    def print(self, k):
        print(self.s[k - 1])

    def undo(self):
        ops = self.ops_stack.pop()
        val = self.val_stack.pop()

        if ops == 1:
            # remove ending substring of length len(val)
            self.s = self.s[:-len(val)]

        if ops == 2:
            # append substring
            self.s += val


if __name__ == '__main__':

    e = Editor()

    # 1 abc
    e.append('abc')
    print(e)
    # 3 3
    e.print(3)
    # 2 3
    e.delete(3)
    print(e)
    # 1 xy
    e.append('xy')
    print(e)
    # 3 2
    e.print(2)
    # 4
    e.undo()
    print(e)
    # 4
    e.undo()
    print(e)
    # 3 1
    e.print(1)
