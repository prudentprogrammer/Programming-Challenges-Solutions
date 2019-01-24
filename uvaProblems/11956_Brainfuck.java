import java.io.*;
import java.util.*;

class Main {
    public static void main (String[] args) {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        
        while(true) {
            try {
                int testCases = Integer.parseInt(bf.readLine());
                for(int i = 1; i <= testCases; i++) {
                    String cmd = bf.readLine();
                    int[] mem = new int[100];
                    int index = 0;
                    for (int j = 0; j < cmd.length(); j++) {
                        char ch = cmd.charAt(j);
                        if (ch == '>') {
                            // Increment the pointer
                            index = (index + 1) % 100;
                        } else if (ch == '<') {
                            // Decrement the pointer
                            index = (index - 1 + 100) % 100;
                        } else if (ch == '+') {
                            // Increment the byte at the pointer
                            mem[index] = (mem[index] + 1) % 256;
                        } else if (ch == '-') {
                            // Decrement the byte at the pointer
                            mem[index] = (mem[index] - 1 + 256) % 256;
                        }
                    } // End of for
                    
                    System.out.printf("Case %d:", i);
        	        for(int j = 0; j < 100; j++)
        	        	System.out.printf(" %02X", mem[j]);
        	        System.out.println();
                    
                }
            } catch (Exception exception) {
                // Break while loop when file ends.
                break;
            }
        }
    }
}
