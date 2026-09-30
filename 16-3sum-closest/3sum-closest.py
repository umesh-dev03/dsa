
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # If this sum is closer to target, update closest
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact target found
                if total == target:
                    return total

                # Need a larger sum
                elif total < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest
        