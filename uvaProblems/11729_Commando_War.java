// Runtime error :( but logic seems right..
// Still debugging but feel free to take a look at the Python version since it is Accepted (AC).

import java.io.*;
import java.util.*;
import java.util.stream.*;

class Soldier implements Comparable<Soldier> {
    int timeToBrief;
    int timeToExecute;
    
    Soldier(int b, int e) {
        timeToBrief   = b;
        timeToExecute = e;
    }
    
    @Override
    public int compareTo(Soldier other) {
        // Sort by descending order.
        return other.timeToExecute - this.timeToExecute;
    }
    
    @Override
    public String toString() {
        return "(" + timeToBrief + "," + timeToExecute + ")";
    }
}

class Main {
    
    private int getMinimumTime(List<Soldier> soldiers) {
        int sum = 0;
        int ans = 0;
        for(Soldier s: soldiers) {
            sum += s.timeToBrief;
            ans = Math.max(ans, sum + s.timeToExecute);
        }
        return ans;
    }
    
    public static void main (String[] args) throws IOException {
        Main m = new Main();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int counter = 1;
        while (true) {
            int testCases = Integer.parseInt(bf.readLine());
            if(testCases == 0) {
                break;
            }
            List<Soldier> soldiers = new ArrayList<>();
            for(int i = 0; i < testCases; i++) {
                int[] nums = Arrays.stream(bf.readLine().split(" "))
                                          .mapToInt(Integer::parseInt)
                                          .toArray();
                soldiers.add(new Soldier(nums[0], nums[1]));
            }
            Collections.sort(soldiers);
            System.out.println("Case " + counter + ": " + m.getMinimumTime(soldiers));
            counter += 1;
        }
    }
}
