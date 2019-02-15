import java.util.*;
import java.io.*;

class Main {
    private int getScore(String test) {
        int prev = 0;
        int res = 0;
        for(int i = 0; i < test.length(); i++) {
            char curr = test.charAt(i);
            if(curr == 'O') {
                prev += 1;
                res += prev;
            } else {
                prev = 0; // Reset prev
            }
        }
        return res;
    }
    
    public static void main (String[] args) throws IOException {
        Main m = new Main();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(bf.readLine());
        for(int i = 0; i < testCases; i++) {
            String currLine = bf.readLine();
            System.out.println(m.getScore(currLine));
        }
    }
}
