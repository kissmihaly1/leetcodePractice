from typing import List


class Day1:
    def removeStars(s: str):
        stack = []
        for letter in s:
            if letter == '*':
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)

    # print(removeStars("kis**kacsa"))

    def palindromeNumber9(x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig

    # print(palindromeNumber9(121))

    def romantointeger13(s: str) -> int:
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


class Day2:
    # We have two special characters:
    # The first character can be represented by one bit 0.
    # The second character can be represented by two bits (10 or 11).
    # Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1


class Day3:
    # 2574. Left and Right Sum Differences
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = [0]
        for i in nums: ans += [ans[-1] + i]
        a = []
        for i in range(1, len(ans)):
            a += [abs(ans[-1] - ans[i] - ans[i - 1])]
        return a


class Day4:
    # 66. Plus One
    def plusOne(digits: List[int]) -> List[int]:
        result = []
        number = 0
        val = 0

        if len(digits) == 1:
            if digits[0] == 9:
                result.append(1)
                result.append(0)
            else:
                result = [digits[0] + 1]
            return result

        for i in range(len(digits)):
            number = digits[i]
            val = val * 10 + number

        val += 1
        result = [int(x) for x in str(val)]

        return result

    # print(plusOne(digits=[9]))


class Day5_apr22:
    # 191. Number of 1 Bits
    def hammingWeight(n: int) -> int:
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

    # hammingWeight(1010)


class Day6_apr23:
    # 1046. Last Stone Weight
    def lastStoneWeight(stones: List[int]) -> int:
        while len(stones)>=2:
            first = 0
            for i in stones:
                if i > first:
                    first = i
            stones.remove(first)
            second = 0
            for i in stones:
                if i > second:
                    second = i
            stones.remove(second)
            if first > second:
                first -= second
                stones.append(first)

            print(stones)
            print(len(stones))
        if len(stones)==1:
            return stones[0]
        else:
            return 0
    lastStoneWeight(stones=[1,3])


class Day7_apr24:
