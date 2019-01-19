import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    
    private void printVertically(List<String> sentences, int maxLength) {
        for(int col = 0; col < maxLength; col++) {
            StringBuilder res = new StringBuilder();
            for(String currSentence: sentences) {
                if(col < currSentence.length()) {
                    res.append(currSentence.charAt(col));
                } else {
                    res.append(" "); // Print space.
                }
            }
            System.out.println(res.reverse().toString());
        }
    }
    
    public static void main (String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        int maxLength = -1;
        Main m = new Main();
        while(true) {
            try {
                String message = bf.readLine();
                maxLength = Math.max(maxLength, message.length());
                lines.add(message);
            } catch (Exception exception) {
                // Break while loop when file ends.
                break;
            }
        }
        m.printVertically(lines, maxLength);
    }
}
