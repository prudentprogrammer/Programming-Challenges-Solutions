import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());

        for(int i = 0; i < testCases; i++) {
            int currNum = Integer.parseInt(br.readLine());
            
            StringBuilder currLine = new StringBuilder();
            for(int times = 1; times <= 10; times++) {
                currLine.append(" " + (currNum * times));
            }
            System.out.println(currLine.toString().trim());
        }
    }
}