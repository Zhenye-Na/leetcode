class Solution {
    public int coinChange(int[] coins, int amount) {
        
        int[] f = new int[amount + 1];
        int n = coins.length;
        
        // Initialization
        f[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            
            f[i] = Integer.MAX_VALUE;
            
            for (int j = 0; j < n; j++) {
                
                if (i - coins[j] >= 0 && f[i - coins[j]] != Integer.MAX_VALUE) {
                    f[i] = Math.min(f[i], f[i - coins[j]] + 1);
                }
                
            }
            
        }
        
        // Double check
        if (f[amount] != Integer.MAX_VALUE) {
            return f[amount];
        } else {
            return -1;
        }
    }
}