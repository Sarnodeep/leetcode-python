class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        right = arr[length - 1]
        arr[length - 1] = -1
        for i in range(length - 2, -1, -1):
            last = arr[i]
            arr[i] = right
            right = arr[i] if last < arr[i] else last
        return arr
