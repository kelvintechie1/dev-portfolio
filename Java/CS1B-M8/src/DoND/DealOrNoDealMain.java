package DoND;
import java.lang.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class DealOrNoDealMain {
    
    public static void pickfirstcase(Cases mycase, Cases valuecases) {

        String t[] = mycase.remainingCases();

        String values = valuecases.valuesRemaining();

        int n = JOptionPane.showOptionDialog(null, values, "Select a case.",
                JOptionPane.YES_NO_CANCEL_OPTION,
                JOptionPane.QUESTION_MESSAGE,
                null, t, t[1]);

        mycase.SwapCases(n + 1, 0);

    }
    public static void pickcases(Cases mycase, Cases valuecases) {
        
        for (int i = 0; i < NumberofCases; i++) {
            String t[] = mycase.remainingCases();

            String values = valuecases.valuesRemaining();

            int n = JOptionPane.showOptionDialog(null, values, "Select a case." + "/ Remaining Cases: " + (NumberofCases - i),
                JOptionPane.YES_NO_CANCEL_OPTION,
                JOptionPane.QUESTION_MESSAGE,
                null, t, t[1]);     
            
            int location = mycase.location(n);
            int valueOfCase = mycase.ValueOfLocation(location);
            JOptionPane.showMessageDialog(null, "The case has a value of " + valueOfCase);
            valuecases.findValue(valueOfCase);            
            mycase.SetLocationto0(location);
        }


    }    
    public static int NumberofCases = 6;
    public static void main(String[] args) {
        Cases cases = new Cases();
        cases.Shuffle();
        Cases cases2 = new Cases();
        int value = 0;
        
        pickfirstcase(cases,cases2);
        boolean allowCases = true;
        while (allowCases == true) {
            pickcases(cases,cases2);
            value = (int) ((cases2.Median() + (int)cases2.Average()) / 2);
            // Define option choices for confirmation dialog
            Object[] options = {"Deal", "No deal"};
            int choose = JOptionPane.showConfirmDialog(null, "The bank's offer is " + value + ". Deal or no deal?");
            if (choose == 0) {
                allowCases = false;
            }
            if (NumberofCases >= 1) {
                NumberofCases = NumberofCases - 1;
            }
        }
        
        if(cases.casesLeft() <= 2) {
            allowCases = false;
        }
        
        // Compare value of case with bank offer and offer different response as appropriate
        int caseValue = cases.ValueOfLocation(0);
        if (caseValue > value) {
            JOptionPane.showMessageDialog(null, "Your case (the case that you chose at the beginning) had $" + caseValue + " in it. Better luck next time.");
        }
        else if (caseValue < value) {
            JOptionPane.showMessageDialog(null, "Your case (the case that you chose at the beginning) had $" + caseValue + " in it. Good job, the bank gave you more than your case had!");
        }
        else {
            JOptionPane.showMessageDialog(null, "Your case (the case that you chose at the beginning) had $" + caseValue + " in it.");
        }
        
    }
    
}
