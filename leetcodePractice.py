

class day1:
    def removeStars(s: str):
        stack=[]
        for letter in s:
            if letter =='*':
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)

    #print(removeStars("kis**kacsa"))


    def palindromeNumber9 (x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig

    #print(palindromeNumber9(121))

    def romantointeger13(s:str) ->int:
            translations = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }
            number = 0
            s = s.replace("IV", "IIII").replace("IX", "VIIII")
            s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
            s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
            for char in s:
                number += translations[char]
            return number
    print(romantointeger13(s="XX"))
