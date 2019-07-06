import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    float A = scanner.nextFloat();
    float B = scanner.nextFloat();
    System.out.println(String.format("MEDIA = %.5f", (3.5 * A + 7.5 * B)/(3.5+7.5)));
  }
}
