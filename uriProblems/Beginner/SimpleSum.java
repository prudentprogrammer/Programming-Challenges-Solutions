import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String line = null;
    int sum = 0;
    while ((line = reader.readLine()) != null) {
      sum += Integer.parseInt(line.trim());
    } // End of while
    System.out.println(String.format("SOMA = %d", sum));
  }
}
