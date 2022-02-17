class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        isPrime = [True for _ in range(n)]
        for i in range(2, math.floor(n**0.5)+1):
            if not isPrime[i]:
                continue
            for j in range(i**2, n, i):
                isPrime[j] = False
        
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
        return cnt
            
