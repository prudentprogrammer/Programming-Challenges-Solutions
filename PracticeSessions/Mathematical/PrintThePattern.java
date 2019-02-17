import java.util.*;
import java.io.*;
import java.lang.*;

class Main {
    private String printNTimes(int N) {
        String res = "";
        for(int lines = N; lines > 0; lines--) {
            String currLine = ""; 
            for(int currNum = N; currNum > 0; currNum--) {
                for(int times = lines; times > 0; times--) {
                    currLine += String.format(" %d", currNum);
                }
            }
            res += (currLine.trim() + " $");
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Main m = new Main();
        int testCases = Integer.parseInt(br.readLine());

        for(int i = 0; i < testCases; i++) {
            System.out.println(m.printNTimes(Integer.parseInt(br.readLine())));
        }
    }
}
