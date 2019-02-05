// Link: https://uva.onlinejudge.org/external/12/1225.pdf
import java.io.*;
import java.util.*;

class Main {
    
    private int getMaxCycleLength (int i, int j) {
        int start = Math.min(i, j);
        int end   = Math.max(i, j);
        
        int maxCycleLength = Integer.MIN_VALUE;
        for(int number = start; number <= end; number++) {
            maxCycleLength = Math.max(maxCycleLength, getCurrentCycleLength(number));
        }
        return maxCycleLength;
    } // End of get max cycle.
    
    private int getCurrentCycleLength(int target) {
        int count = 1;
        
        while (target != 1) {
            if (target % 2 != 0) {
                target = 3 * target + 1;
            } else {
                target = target / 2;
            }
            count += 1;
        } // End of while
        return count;
    } // End of getCurrentCycle
    
    public static void main(String[] args) throws IOException {
        Main m = new Main();
        Scanner in = new Scanner(System.in);
        
        while(in.hasNextInt()) {
            int[] nums = { in.nextInt(), in.nextInt() };
            System.out.println(String.format("%d %d %d", nums[0], nums[1], m.getMaxCycleLength(nums[0], nums[1])));
        } // End of while
    }
}
