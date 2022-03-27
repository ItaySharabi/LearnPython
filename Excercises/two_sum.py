def twoSum(nums: list, target: int) -> list:
    """
    כתבו את תוכן הפונקציה - כך שהיא תחזיר רשימה של שני אינדקסים,
    כך שסכום המספרים הנמצאים באינדקסים האלה שווה למספר המטרה:
    nums = [1, 2, 3, 4],
    target = 6
    output: [1, 3] -->  nums[1] + nums[3] = 2 + 4 = 6
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [1, 2, 2, 4]
target = 4
print(f'twoSum({nums}, {target}) = {twoSum(nums, target)}')
