import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    
    private int getTotalWordsInTheSentence(String sentence) {
        int count = 0;
        boolean areLettersPresentForCurrentWord = false;
        for(int i = 0; i < sentence.length(); i++) {
            char ch = sentence.charAt(i);
            if (Character.isLetter(ch)) {
                areLettersPresentForCurrentWord = true;
            } else { // Other character such as blank space or new line
                if (areLettersPresentForCurrentWord)
                    count += 1;
                areLettersPresentForCurrentWord = false;
            }
        }
        return count;
    }
    
    
    public static void main (String[] args) {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        Main m = new Main();
        while(true) {
            try {
                String message = bf.readLine();
                System.out.println(m.getTotalWordsInTheSentence(message));
            } catch (Exception exception) {
                // Break while loop when file ends.
                break;
            }
        }
    }
}
