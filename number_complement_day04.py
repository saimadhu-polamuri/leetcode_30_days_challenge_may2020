

class Solution:

    def findComplement(self, num: int) -> int:

        if num == 0:
            number= self.bit_complement(num)
        else:
            remiders = list()
            while num >= 1:
                reminder = num % 2
                num = num // 2
                remiders.append(self.bit_complement(reminder))
            number = self.binary_to_decimal(remiders)
        return number

    def bit_complement(self, bit):

        return 1 - bit

    def binary_to_decimal(self, binary_array):

        array_len = len(binary_array)
        number = 0

        for i in range(array_len-1, -1, -1):

            number = number +  binary_array[i] * pow(2, i)
        return number


test_solution = Solution()

print(test_solution.findComplement(1))

# print(test_solution.get_bit_complement(0))
