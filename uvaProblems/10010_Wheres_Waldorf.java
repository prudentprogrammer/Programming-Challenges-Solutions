// Link: https://uva.onlinejudge.org/external/100/10010.pdf

import java.io.*;
import java.util.*;

class Main {
    
    private int[][] dirs;
    
    public Main() {
        // Initialize the 8 directions.
        this.dirs = new int[8][2];
        int idx = 0;
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0)
                    continue;
                dirs[idx][0] = i;
                dirs[idx][1] = j;
                idx += 1;
            }
        }    
    }
    
    private String getCoordinates(List<String> grid, String word, int rows, int cols) {
        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                for(int[] d: dirs) {
                    int i = row, j = col;
                    int idx = 0;
                    //System.out.println(grid.get(i).charAt(j) + "," + word.charAt(idx));
                    while(grid.get(i).charAt(j) == word.charAt(idx)) {
                        i += d[0];
                        j += d[1];
                        //System.out.println(nextX + "," + nextY);
                        idx += 1;
                        
                        if (idx == word.length()) {
                            return String.format("%d %d", row + 1, col + 1);
                        }
                        if (i < 0 || i >= rows || j < 0 || j >= cols) {
                            break; // Out of bounds, invalid!
                        }
                    }
                } // End of for
            } // End of cols loop
        } // End of rows loop
        
        return "";
    }
    
    
    public static void main (String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      Main m = new Main();
      int totalCases = Integer.parseInt(br.readLine());
      for(int i = 1; i <= totalCases; i++) {

        br.readLine(); // Skip the blank line
        int[] nums = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
        int rows = nums[0], cols = nums[1];
        List<String> grid = new ArrayList<>();
        for (int row = 0; row < rows; row++) {
            grid.add(br.readLine().toLowerCase());
        }

        int words = Integer.parseInt(br.readLine());
        for(int j = 0; j < words; j++) {
            String currWord = br.readLine().toLowerCase();
            System.out.println(m.getCoordinates(grid, currWord, rows, cols));
        }

        if (i < totalCases) {
            System.out.println(); // Print a new line at the end
        } // End of if
      } // End of for
    } // End of main
}
