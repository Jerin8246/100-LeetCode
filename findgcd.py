# 1. The Euclidean Algorithm (Fastest Method) This method uses division to find the greatest factor that divides two numbers without a remainder. \

# Step 1: Divide the larger number by the smaller number.
# Step 2: Take the remainder from that division and divide the previous divisor by this remainder.Step 3: Repeat this process until the remainder is 0.Result: The last non-zero remainder is the GCD. 

# Example: GCD(48, 18) 
#  1. (48 ÷ 18 = 2 ) with a remainder of (12) 
#  2. (18 ÷ 12 = 1) with a remainder of (6)
#  3. (12 ÷ 6 = 2) with a remainder of (0) 
#  4. The last non-zero remainder is 6. 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            
            return len1

        return str1[:gcd(len(str1), len(str2))]

        