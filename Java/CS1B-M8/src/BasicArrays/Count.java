package BasicArrays;
import java.util.*;
public class Count {

    public static void Count(int[] Array, int big) {
        Integer count = 0;
        Integer arrayLength = Array.length;
        for (int i = 0; i < arrayLength; i++) {
            if (Array[i] > big) {
                count = count + 1;                
            }
        }
        System.out.println(count);
        
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
        System.out.println("Enter a number to check for how many numbers in your array is larger than that number.");
        int big = input.nextInt();
        Count(TestArray, big);
    }
    
}