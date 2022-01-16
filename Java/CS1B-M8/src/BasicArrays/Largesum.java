package BasicArrays;
import java.util.*;
public class Largesum {
    
    public static void Largesum(int[] Array, int big) {
        Integer sum = 0;
        Integer arrayLength = Array.length;
        for (int i = 0; i < arrayLength; i++) {
            if (Array[i] > big) {
                sum = sum + Array[i];                
            }
        }
        System.out.println(sum);
        
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
        System.out.println("Enter a number to check for the sum of all numbers in your array that are larger than that number.");
        int big = input.nextInt();
        Largesum(TestArray, big);
    }
    
}
