import string


class day1:
    def removeStars(s: string):
        stack=[]
        for letter in s:
            if letter =='*':
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)

    print(removeStars("kis**kacsa"))



