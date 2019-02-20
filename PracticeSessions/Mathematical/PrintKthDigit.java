import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());

        for(int i = 0; i < testCases; i++) {
            int[] nums = Arrays.stream(br.readLine().trim().split("\\s+"))
                               .mapToInt(Integer::parseInt)
                               .toArray();
            String total = "" + ((long)(Math.pow(nums[0], nums[1])));
            System.out.println(total.charAt(total.length() - nums[2]));
        } // End of for
    }
}