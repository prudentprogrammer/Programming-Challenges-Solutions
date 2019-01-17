// Link: https://uva.onlinejudge.org/external/4/458.pdf

import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main (String[] args) {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            try {
                String message = bf.readLine();
                final int offset = 7; // This value was figured out using the example.
                StringBuilder res = new StringBuilder();
                for(int i = 0; i < message.length(); i++)
                    res.append("" + (char)(message.charAt(i) - offset));
                System.out.println(res.toString());
            } catch (Exception exception) {
                // Break while loop when file ends.
                break;
            }
        }
    }
}
