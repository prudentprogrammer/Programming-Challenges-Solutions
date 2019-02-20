import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
    private int gcd(int a, int b) {
      if(a == 0){
        return b;
      } else {
        return gcd(b % a, a);
      }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        Main m = new Main();

        for(int i = 0; i < testCases; i++) {
          int a = sc.nextInt();
          int b = sc.nextInt();
          System.out.println(m.gcd(a, b));
        }
        sc.close();
    }
}