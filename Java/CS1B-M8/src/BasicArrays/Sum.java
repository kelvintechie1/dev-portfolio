package BasicArrays;
import java.util.*;
public class Sum {
    
    public static void Sum(int[] Array, int first, int last) {
        Integer sum = 0;
        Integer arrayLength = Array.length;
        for (int i = first; i <= last; i++) {
            sum = sum + Array[i];
        }
        System.out.println(sum.toString());
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter 10 integers.");
        Integer inputNum = 0;
        int TestArray[] = new int[10];
        for (int i = 0; i < 10; i++) {
            inputNum = input.nextInt();
            TestArray[i] = inputNum;
        }
        System.out.println("Enter the position of the number that you want to begin at (from 0 being the first to 9 being the last number).");
        Integer firstPosition = input.nextInt();
        System.out.println("Enter the position of the number that you want to end at (from 0 being the first to 9 being the last number).");
        Integer lastPosition = input.nextInt();        
        Sum(TestArray, firstPosition, lastPosition);
    }
}
    