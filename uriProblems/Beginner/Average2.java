import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    float A = scanner.nextFloat();
    float B = scanner.nextFloat();
    float C = scanner.nextFloat();
    System.out.println(String.format("MEDIA = %.1f", (2 * A + 3 * B + 5 * C)/10));
  }
}
