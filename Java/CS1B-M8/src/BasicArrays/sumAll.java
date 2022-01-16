package BasicArrays;
import java.util.*;
public class sumAll {
    
    public static void sumAll(int[] Array) {
        Integer sum = 0;
        Integer arrayLength = Array.length;
        for (int i = 0; i < arrayLength; i++) {
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
        sumAll(TestArray);
    }
    
}
