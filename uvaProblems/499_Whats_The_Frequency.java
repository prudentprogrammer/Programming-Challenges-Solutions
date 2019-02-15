// Link: https://uva.onlinejudge.org/external/4/499.pdf
import java.io.*;
import java.util.*;

class Main {
    
    private String getHighestFrequencyLetters(String line) {
        HashMap<Character, Integer> counter = new HashMap<>();
        int maxCount = Integer.MIN_VALUE;
        for(int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (!Character.isAlphabetic(ch))
                continue; // Skip non-alphabet characters.
            if (counter.containsKey(ch)) {
                counter.put(ch, counter.get(ch) + 1);
            } else {
                counter.put(ch, 1);
            }
        } // End of for
        
        for (Integer value : counter.values()) {
            maxCount = Math.max(maxCount, value);
        }
        
        List<String> chars = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : counter.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            if (value == maxCount) {
                chars.add("" + key);
            }
        } // End of for
        
        Collections.sort(chars); 
        String highestChars = String.join("", chars);
        return String.format("%s %d", highestChars, maxCount);
    }
    
    
  public static void main (String[] args) throws IOException {
      Main m = new Main();
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      String s = "";

      while((s = br.readLine()) != null) {
          System.out.println(m.getHighestFrequencyLetters(s));
      } // End of while
  }
}
