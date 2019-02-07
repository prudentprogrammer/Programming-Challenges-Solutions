// Link: https://uva.onlinejudge.org/external/9/902.pdf
import java.io.*;
import java.util.*;

class Main {
    
    private String getHighestFrequencySubstring(int N, String line) {
        HashMap<String, Integer> counter = new HashMap<>();
        int maxCount = Integer.MIN_VALUE;
        for(int i = 0; i < (line.length() + 1 - N); i++) {
            String sub = line.substring(i, i + N);
            if (counter.containsKey(sub)) {
                counter.put(sub, counter.get(sub) + 1);
            } else {
                counter.put(sub, 1);
            }
        } // End of for
        
        for (Integer value : counter.values()) {
            maxCount = Math.max(maxCount, value);
        }
        
        String commonSubstring = "";
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            if (value == maxCount) {
                commonSubstring = key;
                break;
            }
        } // End of for
        
        return commonSubstring;
    }
    
    
  public static void main (String[] args) throws IOException {
      Main m = new Main();
      Scanner s = new Scanner(System.in);

      while(s.hasNext()) {
          int N = s.nextInt();
          String word = s.next();
          System.out.println(m.getHighestFrequencySubstring(N, word));
      } // End of while
  }
}
