import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
    
    private int linearSearch(int[] nums, int target) {
       for(int i = 0; i < nums.length; i++) {
          if (nums[i] == target) {
             return i;
          } // End of if
       }
       return -1;
    } 
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Main m = new Main();
        int testCases = Integer.parseInt(br.readLine());

        for(int i = 0; i < testCases; i++) {
            br.readLine(); // Omit the number of elements in the given array.
            int[] nums = Arrays.stream(br.readLine().split("\\s+"))
                               .mapToInt(Integer::parseInt)
                               .toArray();
            int target = Integer.parseInt(br.readLine());
            System.out.println(m.linearSearch(nums, target));
        } // End of for
    } 
}
