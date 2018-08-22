class Solution {
    public int findPeakElement(int[] nums) {

        int start = 0, end = nums.length - 1;
        
        while (start + 1 < end) {
            
            int mid = (end - start) / 2 + start;
            
            if (nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1]) {         // Ascending section
                start = mid;
            } else if (nums[mid - 1] > nums[mid] && nums[mid] > nums[mid + 1]) {  // Descending section
                end = mid;
            } else if (nums[mid - 1] > nums[mid] && nums[mid] < nums[mid + 1]) {  // Valley
                end = mid;
            } else {                                                              // Peak
                return mid;
            }

        }
        
        if (nums[start] < nums[end]) {
            return end;
        } else {
            return start;
        }

    }
}