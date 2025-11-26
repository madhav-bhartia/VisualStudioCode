class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        results = []
        for i in range(n-k+1):
            subarray = nums[i:i+k]
            appended = False
            if not appended:
                for i in range(len(subarray)-1):
                    if (subarray[i]+1) == subarray[i + 1]:
                        pass
                    else:
                        results.append(-1)
                        appended = True
                        break
            else:
                continue
            if not appended:
                if subarray == sorted(subarray):
                    results.append(max(subarray))
                    appended = True
                else:
                    results.append(-1)
                    appended = True
            else:
                continue
        return results