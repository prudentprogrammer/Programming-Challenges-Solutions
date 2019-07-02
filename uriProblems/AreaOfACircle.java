import java.util.*;
import java.util.stream.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    double radius = Double.parseDouble(br.readLine());
    System.out.println(String.format("A=%.4f", 3.14159 * (radius * radius)));
  }
}
