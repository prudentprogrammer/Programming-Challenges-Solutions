import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    private int getNumberOfCoins(PriorityQueue<Integer> dragonHeads, 
                                 PriorityQueue<Integer> knights) {
        if (dragonHeads.size() > knights.size()) {
            return -1; // Doomed!
        }
        int result = 0;
        while(!knights.isEmpty()) {
            if(dragonHeads.isEmpty()) {
                return result;
            }
            
            int smallest_knight = knights.poll();
            if(dragonHeads.peek() <= smallest_knight) {
                result += smallest_knight;
                dragonHeads.poll(); // Cut off the dragon head.
            }
            
        }
        if(dragonHeads.isEmpty()) {
            return result;
        }
        return -1;
    }
    
    
    public static void main (String[] args) throws IOException {
        Main m = new Main();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> dragonHeads = null;
        PriorityQueue<Integer> knights = null;
        
        while(true) {
            int[] currLine = Arrays.stream(bf.readLine().split(" "))
                                          .mapToInt(Integer::parseInt)
                                          .toArray();
            if (currLine[0] == 0 && currLine[1] == 0)
                break;
            
            dragonHeads = new PriorityQueue<>();
            knights =  new PriorityQueue<>();
            for(int i = 0; i < currLine[0]; i++)
                dragonHeads.add(Integer.parseInt(bf.readLine()));
            
            for(int i = 0; i < currLine[1]; i++)
                knights.add(Integer.parseInt(bf.readLine()));

            int result = m.getNumberOfCoins(dragonHeads, knights);
            if(result == -1) {
                System.out.println("Loowater is doomed!");
            } else {
                System.out.println(result);
            }
        }
    }
}
