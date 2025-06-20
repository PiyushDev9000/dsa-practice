class Solution:

    def aggressiveCows(self, stalls, k):
        
        
        def canweplace(arr, cows, dist):
            
            currCow = 1 
            last = arr[0]
            
            for i in range(1, len(arr)):
                if((arr[i] - last ) >= dist):
                    currCow+=1
                    last = arr[i]
                    
            
            if currCow >= cows:
                return True
            else:
                return False
            
        
        
        
        stalls.sort()
        # your code here
        low = 1
        high = stalls[len(stalls) - 1] - stalls[0]
        ans = -1
        
        while(low<=high):
            mid = (low + high) // 2
            
            if( canweplace(stalls, k, mid)  == True ):
                ans = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return ans        