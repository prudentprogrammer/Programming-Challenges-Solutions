import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String line = null;
    int product = 1;
    while ((line = reader.readLine()) != null) {
      product *= Integer.parseInt(line.trim());
    } // End of while
    System.out.println(String.format("PROD = %d", product));
  }
}
