// Link: https://uva.onlinejudge.org/external/15/1583.pdf

import java.util.*;
import java.io.*;

class Main {
    private int[] cache;
    private final int MAX_ITEMS = 100001;
    
    public Main() {
        cache = new int[MAX_ITEMS];
        Arrays.fill(cache, Integer.MAX_VALUE);
        for(int num = 1; num <= MAX_ITEMS; num++) {
            // For ex: if num is 198
            // 198 + getSum(198) => 216
            // cache[216] = min(cache[216], 198)
            int generatedNum = num + getSum(num);
            if (generatedNum < MAX_ITEMS) {
                cache[generatedNum] = Math.min(num, cache[generatedNum]);
            }
        }
    }
     
    private int getSmallestGenerator(int target) {
        return (target >= MAX_ITEMS || cache[target] == Integer.MAX_VALUE) ? 0 : cache[target];
    }
    
    private int getSum(int num) {
        int sum = 0;
        
        while (num != 0) {
            sum += num % 10;
            num = num / 10;
        }
        return sum;
    }
    
    public static void main (String[] args) throws IOException {
        Main m = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());
        for(int i = 0; i < testCases; i++) {
            System.out.println(m.getSmallestGenerator(Integer.parseInt(br.readLine())));
        }
    }
}
