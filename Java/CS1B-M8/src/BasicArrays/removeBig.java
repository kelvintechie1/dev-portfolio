package BasicArrays;
import java.util.*;
public class removeBig {
    
    public static void removeBig(int[] Array, int big) {
        Integer sum = 0;
        String FinalString = "";
        Integer arrayLength = Array.length;
        Integer newArrayLength = 0;
        for (int i = 0; i < arrayLength; i++) {
            if (Array[i] > big) {
                Array[i] = 0;             
            }
        }
       
        for (int j = 0; j < arrayLength; j++) {
            if (Array[j] != 0) {
                newArrayLength = newArrayLength + 1;
            }
        }
        
        int[] newArray = new int[newArrayLength];
        
        for (int k = 0; k < arrayLength; k++) {
            if (Array[k] != 0) {
                newArray[k] = Array[k];
            }
        }
        
        for (int l = 0; l < newArrayLength; l++) {
            FinalString = FinalString + newArray[l] + " ";
        }
        System.out.println(FinalString);
        
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
        System.out.println("Enter a number to return an updated array with all numbers larger than this number removed.");
        int big = input.nextInt();
        removeBig(TestArray, big);
    }
    
}
