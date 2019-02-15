import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main (String[] args) {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            try {
                long[] nums = Arrays.stream(bf.readLine().split(" "))
                                   .mapToLong(Long::parseLong)
                                   .toArray();
                System.out.println(nums[1] > nums[0] ? nums[1] - nums[0] : nums[0] - nums[1]);
            } catch (Exception exception) {
                // Break while loop when file ends.
                break;
            }
        }
    }
}
