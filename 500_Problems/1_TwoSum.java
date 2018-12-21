import java.util.HashMap;

// Find a pair with a given sum in the array.

class TwoSum {
  
  private static int[] findPair(int[] nums, int target) {
    
    HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();

    for(int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];

      if (numMap.containsKey(complement)) {
        return new int[] { numMap.get(complement), i };
      } else {
        numMap.put(nums[i], i);
      }
    } // End of for

    return new int[] { -1 } ;
  } // End of findPair


  public static void main (String[] args) {
    int[] nums = { 8, 7, 2, 5, 3, 1 };
    int sum = 10;

    TwoSum t = new TwoSum();
    int[] indices = t.findPair(nums, sum);
    for (int index: indices) {
      System.out.print("Pair found at index " + index + ".\n");
    }

  } // End of main

}
