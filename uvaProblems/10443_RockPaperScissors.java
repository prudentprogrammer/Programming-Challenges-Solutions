import java.io.*;
import java.util.*;

class Main {
  private int[][] dirs = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
  private HashMap<String, String> winningLifeFormMap = new HashMap<>();
  private String[][] grid;
  private int rows, cols, days;

  Main(int rows, int cols, int days, String[][] grid) {
    winningLifeFormMap.put("R", "P");
    winningLifeFormMap.put("S", "R");
    winningLifeFormMap.put("P", "S");

    this.rows = rows;
    this.cols = cols;
    this.days = days;
    this.grid = grid;
  }

  private String getWinningNeighbor(int i, int j) {
    String winningLifeForm = grid[i][j];

    for(int[] dir: dirs) {
      int dx = dir[0], dy = dir[1];
      int nextX = dx + i, nextY = dy + j;
      if (nextX >= 0 && nextX < rows && nextY >= 0 && nextY < cols) {
        if (winningLifeFormMap.get(grid[i][j]).equals(grid[nextX][nextY])) {
          winningLifeForm = winningLifeFormMap.get(grid[i][j]);
        }
      } // End of if
    }
    return winningLifeForm;
  }

  private void printGrid(String[][] grid) {
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++)
        System.out.print(grid[i][j]);
      System.out.println();
    }
  }

  private void simulate () {

    for(int t = 0; t < days; t++) {
      String[][] copy = new String[rows][cols];
      for(int row = 0; row < rows; row++) {
        for(int col = 0; col < cols; col++) {
          copy[row][col] = getWinningNeighbor(row, col);
        }
      }
      grid = copy;
    }

    printGrid(grid);
  }

  public static void main (String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int testCases = Integer.parseInt(br.readLine());

    for(int currentLine = 1; currentLine <= testCases; currentLine++) {

      int[] nums = Arrays.stream(br.readLine().split(" "))
                         .mapToInt(Integer::parseInt)
                         .toArray();
      if (nums[0] == 0 && nums[1] == 0) {
        br.readLine();
        continue;
      }
      else {
        String[][] grid = new String[nums[0]][nums[1]];
        for(int i = 0; i < nums[0]; i++) {
          grid[i] = br.readLine().split("");
        }

        Main rps = new Main(nums[0], nums[1], nums[2], grid);
        rps.simulate();
      }

      if (currentLine != testCases) {
        System.out.println();
      }
    } // End of for
  } // End of main
}
