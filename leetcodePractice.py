from typing import List


class Day1:
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


class Day2:
    #We have two special characters:
    #The first character can be represented by one bit 0.
    #The second character can be represented by two bits (10 or 11).
    #Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.


    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1


class Day3:
    #2574. Left and Right Sum Differences
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans=[0]
        for i in nums: ans+=[ans[-1]+i]
        a=[]
        for i in range(1,len(ans)):
            a+=[abs(ans[-1]-ans[i]-ans[i-1])]
        return a



