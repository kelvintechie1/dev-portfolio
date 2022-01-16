package cs1b.m10;
import java.util.*;
import java.text.*;

public class MakeChange {
    
    public static double TotalChange(double sale, double paid) {
        double change = paid - sale;
        return change;
    }
    
    public static int Dollars(double change) {
        int dollars = (int) change;
        return dollars;
    }
    
    public static double Quarters(double change) {
        double quarters = 0;
        for (int i = 1; i < 4; i++) {
            if (0.25 * i <= change) {
                quarters = i;
            }
            else if (0.25 * i > change) {
                break;
            }
        }
        return quarters;
    }
    
    public static double Dimes(double change) {
        double dimes = 0;
        for (int i = 1; i < 10; i++) {
            if (0.1 * i <= change) {
                dimes = i;
            }
            else if (0.1 * i > change) {
                break;
            }
        }
        return dimes;
    }
        
    public static double Nickels(double change) {
        double nickels = 0;
        for (int i = 1; i < 20; i++) {
            if (0.05 * i <= change) {
                nickels = i;
            }
            else if (0.05 * i > change) {
                break;
            }
        }
        return nickels;
    }
    
    public static double Pennies(double change) {
        double pennies = 0;
        for (int i = 1; i < 100; i++) {
            if (0.01 * i <= change) {
                pennies = i;
            }
            else if (0.01 * i > change) {
                break;
            }
        }
        return pennies;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter the sale amount (up to two decimal places for sub-dollar amounts).");
        double sale = input.nextDouble();
        System.out.println("Please enter the amount tendered in dollars (up to two decimal places for sub-dollar amounts).");
        double money = input.nextDouble();
        double OriginalChangeAmount = 0.0;
        double UpdatedChangeAmount = 0.0;
        if (sale > money) {
            System.out.println("No change required. The money tendered is less than the sale amount.");
        }
        else if (sale == money) {
            System.out.println("No change required. The money tendered is the same as the sale amount.");
        }
        else if (sale < money) {
            NumberFormat nf = NumberFormat.getInstance();
            nf.setMaximumFractionDigits(2);            
            OriginalChangeAmount = TotalChange(sale, money);
            String updatedStr = nf.format(OriginalChangeAmount);
            UpdatedChangeAmount = Double.parseDouble(updatedStr);
            System.out.println("Total Change: $" + nf.format(UpdatedChangeAmount));
            System.out.println("Change (dollars): " + nf.format(Dollars(UpdatedChangeAmount)));
            UpdatedChangeAmount = UpdatedChangeAmount - Dollars(UpdatedChangeAmount);
            System.out.println("Change (quarters): " + nf.format(Quarters(UpdatedChangeAmount)));
            UpdatedChangeAmount = UpdatedChangeAmount - (Quarters(UpdatedChangeAmount) * .25);
            System.out.println("Change (dimes): " + nf.format(Dimes(UpdatedChangeAmount)));
            UpdatedChangeAmount = UpdatedChangeAmount - (Dimes(UpdatedChangeAmount) * .10);
            System.out.println("Change (nickels): " + nf.format(Nickels(UpdatedChangeAmount)));
            UpdatedChangeAmount = UpdatedChangeAmount - (Nickels(UpdatedChangeAmount) * .05);
            System.out.println("Change (pennies): " + nf.format(Pennies(UpdatedChangeAmount)));
            UpdatedChangeAmount = UpdatedChangeAmount - (Pennies(UpdatedChangeAmount) * .01);
        }
        else {
            System.out.println("Please enter a valid amount.");
        }
    }
    
}
