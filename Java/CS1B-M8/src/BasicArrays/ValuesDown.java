package BasicArrays;
import java.util.*;
public class ValuesDown {
    
    public static void ValuesDown(int[] Array) {
        Integer sum = 0;
        Integer arrayLength = Array.length;
        Boolean[] smaller = new Boolean[arrayLength - 1];
        for (int i = 0; i < arrayLength - 1; i++) {
            if (Array[i] < Array[i+1]) {
                smaller[i] = true;
            }
            else {
                smaller[i] = false;
            }
        }
        for (int j = 0; j < arrayLength - 1; j++) {
            System.out.println("The number at position " + (j + 1) + " is smaller than " + (j + 2) + " - " + smaller[j].toString());
        }
        
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
        ValuesDown(TestArray);
    }
    
}
