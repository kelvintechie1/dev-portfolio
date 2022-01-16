package cs1b.m10;
import java.util.*;
public class Fibonacci {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter how many numbers you want your fibonacci series to have.");
        int number = input.nextInt();
        int[] series = new int[number];
        System.out.println("Enter what number you want your fibonacci series to begin on. (Recommended: 0)");
        int firstNum = input.nextInt();
        series[0] = firstNum;
        series[1] = firstNum + 1;
        for (int i = 2; i < number; i++) {
            series[i] = series[i - 2] + series[i - 1];
        }
        String FinalString = "";
        for (int i = 0; i < series.length; i++) {
            FinalString = FinalString + series[i] + " ";
        }
        System.out.println(FinalString);
    }
    
}
