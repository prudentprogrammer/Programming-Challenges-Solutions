import java.util.*;

class SubarrayZero {
  
  // Helper function
  private static boolean subArrayExists(int[] nums) {
    Set<Integer> seen = new HashSet<Integer>();
    seen.add(0);

    int sum = 0;
    for(int num: nums) {
      sum += num;

      if (seen.contains(sum)) {
        return true;
      }
      seen.add(sum);
    } // End of for

    return false;
  }

  private static List<List<Integer>> subarrays(int[] nums) {

    List<List<Integer>> result = new ArrayList<>();
    HashMap<Integer, List<Integer>> seen = new HashMap<>();
    seen.putIfAbsent(0, Arrays.asList(new int[] {-1} ));

    int sum = 0;
    for(int i = 0; i < nums.length; i++) {
      sum += nums[i];

      if (seen.containsKey(sum)) {
        List<Integer> indices = seen.get(sum);

        for(Integer index: indices) {
          int[] temp = new int[] { index + 1, i };
          result.add(Arrays.asList(temp));
        } // End of for

        seen.putIfAbsent(sum, new ArrayList<Integer>());
        seen.get(sum).add(i);
      }

    } // End of for

    return result;
  } 



  public static void main (String[] args) {
    
    int[] nums = { 4, 3, 2, -4, -1 };
    
    SubarrayZero s = new SubarrayZero();
    System.out.println(s.subArrayExists(nums));

  } // End of main

}
