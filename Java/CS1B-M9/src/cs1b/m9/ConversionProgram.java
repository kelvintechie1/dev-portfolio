package cs1b.m9;
import java.util.*;
public class ConversionProgram {
    public static String ConversionToBinary(int num) {
        String result = "";
        int largestNum = 0;
        boolean largestFound = false;
        for (int i = 0; i < 100; i++) {
            if ((int) Math.pow(2,(double) (i)) >= num ) {
                largestNum = (int) Math.pow(2,(double) (i));
                break;
            }
        }
        int temp = largestNum;
        int whileCheck = largestNum;
        int whileCounter = 1;
        while (whileCheck != 1) {
            whileCheck = whileCheck / 2;
            whileCounter++;
        }
        int[] binaryNums = new int[whileCounter];
        binaryNums[0] = largestNum;
        for (int i = 1; i < whileCounter; i++) {
            temp = temp / 2;
            binaryNums[i] = temp;
        }
        for (int i = 0; i < whileCounter; i++) {
            if (num >= binaryNums[i]) {
                result = result + "1";
                num = num - binaryNums[i];
            }
            else if (num <= binaryNums[i]) {
                result = result + "0";
            }
        }
        return result;
    }
    
    public static int ConversionToDecimal(String num) {
        int result = 0;
        int length = num.length();
        int tempVar = 0;
        int backwardsPosition = (length - 1);
        for (int i = 0; i < length; i++) {
            if (num.charAt(i) != '0' && num.charAt(i) != '1') {
                System.out.println("Please re-enter a valid binary number.");
                break;
            }
            else if (num.charAt(i) == '1') {
                tempVar = (int) Math.pow((double) 2, (double) backwardsPosition);
                result = result + tempVar;
            }
            backwardsPosition--;
        }
        return result;
        }

        
    public static void main(String[] args) {
        // Ask user to input two integers to convert from decimal to binary and vice versa
        Scanner input = new Scanner(System.in);
        
        System.out.println("Please enter an integer number to convert from binary to decimal.");
        String BtoD = input.nextLine();
        
        System.out.println("Please enter an integer number to convert from decimal to binary.");
        int DtoB = input.nextInt();

        System.out.println("The binary number you entered (" + BtoD + ") in decimal is " + ConversionToDecimal(BtoD) + ".");
        System.out.println("The decimal number you entered (" + DtoB + ") in binary is " + ConversionToBinary(DtoB) + ".");
    }   
        
    }
    

    
