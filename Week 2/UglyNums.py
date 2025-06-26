#ugly nums 1 and 2 brute approch (TLC)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def is_ugly(u):
            for i in [2,3,5]:
                while u % i == 0:
                    u//=i

            return u == 1

        uglyNums = [1]
        num = 2  

        while len(uglyNums) < n:
            if is_ugly(num):
                uglyNums.append(num)
            num += 1

        return uglyNums[-1]     

#ugly nums 2 Better Approch
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
            uglyNums = [1]
            i2 = i3 = i5 = 0

            while len(uglyNums) < n:
                next2 = uglyNums[i2] * 2
                next3 = uglyNums[i3] * 3
                next5 = uglyNums[i5] * 5

                ugly_num = min(next2, next3, next5)
                uglyNums.append(ugly_num)

                if ugly_num == next2:
                    i2 += 1
                if ugly_num == next3:
                    i3 += 1
                if ugly_num == next5: 
                    i5 += 1

            return uglyNums[-1]                                               

