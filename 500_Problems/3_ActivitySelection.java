import java.util.*;

class Interval {
  
  int start;
  int end;
  
  public Interval(int start, int end) {
    this.start = start;
    this.end = end;
  }

  @Override
  public String toString() {
    return "(" + start + "," + end + ")";
  } // End of toString

} // End of interval


class ActivitySimulation {


  // Private method
  private static List<Interval> selectActivities(List<Interval> intervals) {
    List<Interval> result = new ArrayList<Interval>();

    result.add(intervals.get(0));

    for (int i = 1; i < intervals.size(); i++) {
      if ( result.get(result.size() - 1).end <= intervals.get(i).start ) {
        result.add(intervals.get(i));
      }  
    }  

    return result;
  }


  public static void main (String[] args) {
    ActivitySimulation a = new ActivitySimulation();

    List<Interval> intervals = new ArrayList<Interval>(Arrays.asList(
      new Interval(3, 5),
      new Interval(1, 4),
      new Interval(2, 3),
      new Interval(5, 7)
    ));

    Collections.sort(intervals, (f, o) -> f.end - o.end);
    System.out.println(a.selectActivities(intervals));

  } // End of main

} // End of ActivitySimulation
