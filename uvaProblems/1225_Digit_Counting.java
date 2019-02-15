// Link: https://uva.onlinejudge.org/external/12/1225.pdf
import java.io.*;
import java.util.*;

class Main {
    private void printDigitCount(int target) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <= target; i++) {
            sb.append(i);
        }
        
        for (int i = 0; i < sb.length(); i++) {
            int ch = Integer.parseInt("" + sb.charAt(i));
            if (counter.containsKey(ch)) {
                counter.put(ch, counter.get(ch) + 1);
            } else {
                counter.put(ch, 1);
            }
        } // End of for
        
        for(int i = 0; i < 10; i++) {
            if (i == 0) {
                System.out.printf("%d", counter.getOrDefault(0, 0));
            } else if (i == 9) {
                System.out.printf(" %d\n", counter.getOrDefault(9, 0));
            } else {
                System.out.printf(" %d", counter.getOrDefault(i, 0));
            }
        } // End of for
    }
    
    public static void main(String[] args) throws IOException {
        Main m = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < testCases; i++) {
            m.printDigitCount(Integer.parseInt(br.readLine()));
        }
    } // End of main
}
