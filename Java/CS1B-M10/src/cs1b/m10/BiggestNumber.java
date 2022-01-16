package cs1b.m10;
import java.util.*;
import java.io.*;
public class BiggestNumber {
    
    public static double ReturnLargest(double[] array) {
        double largest = Math.max(Math.max(array[0],array[1]), array[2]);
        return largest;
    }
    
    public static void ReadFromKeyboard() {
        Scanner keyb = new Scanner(System.in);
        System.out.println("Please enter three numbers to find out which is the largest.");
        double[] numbers = new double[3];
        for (int i = 0; i < 3; i++) {
            numbers[i] = keyb.nextDouble();
        }
        
        PrintNumbers(ReturnLargest(numbers));
    }
    
    public static void ReadFromFile() throws IOException {
        Scanner keyb = new Scanner(System.in);
        System.out.println("Please enter the name of the file with the file extension that the numbers should be read from? Note that the 3 numbers " +
                "should be line-delimited.");
        String fileName = keyb.nextLine();
        Scanner file = new Scanner(new File(fileName));
        
        double[] numbers = new double[3];
        for (int i = 0; i < 3; i++) {
            numbers[i] = file.nextDouble();   
        }
        
        PrintNumbers(ReturnLargest(numbers));
    }
    
    public static void PrintNumbers(double number) {
        System.out.println("The largest number of the three that were given is: " + number);       
    }
    public static void main(String[] args) throws IOException {
        Scanner keyb = new Scanner(System.in);
        System.out.println("Please choose whether to read numbers from a keyboard input or read numbers from a file. Type \"keyboard\" or \"file\" only.");
        String choice = (keyb.nextLine());
        
        if (choice.equals("keyboard")) {
            ReadFromKeyboard();
        }
        else if (choice.equals("file")) {
            ReadFromFile();
        }
        else {
            System.out.println("Please enter a valid choice.");
        }
    }
    
}
