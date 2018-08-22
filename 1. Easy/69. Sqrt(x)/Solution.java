class Solution {
    public int mySqrt(int x) {
        if (x < 0) return -1;
        if (x == 0) return 0;

        long start = 1, end = x;
        
        while (start + 1 < end) {
            
            long mid = (end - start) / 2 + start;
            long mul = mid * mid;

            if (mul < x) {
                start = mid;
            } else if (mul > x) {
                end = mid;
            } else if (mul == x) {
                return (int)mid;
            }
        }

        if (start * start <= x) {
            return (int)start;
        } else {
            return (int)end;
        }
    }
}