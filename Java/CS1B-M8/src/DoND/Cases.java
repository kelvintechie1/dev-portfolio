package DoND;
public class Cases {
    
    public int[] cases;
    
    public Cases () {
        cases = new int[27];
        cases[0] = 0;
        cases[1] = 1;
        cases[2] = 2;
        cases[3] = 5;
        cases[4] = 10;
        cases[5] = 25;
        cases[6] = 50;
        cases[7] = 75;
        cases[8] = 100;
        cases[9] = 200;
        cases[10] = 300;
        cases[11] = 400;
        cases[12] = 500;
        cases[13] = 750;
        cases[14] = 1000;
        cases[15] = 5000;
        cases[16] = 10000;
        cases[17] = 25000;
        cases[18] = 50000;
        cases[19] = 75000;
        cases[20] = 100000;
        cases[21] = 200000;
        cases[22] = 300000;
        cases[23] = 400000;
        cases[24] = 500000;
        cases[25] = 750000;
        cases[26] = 1000000;
    }
    
    public String toString() {
        String values = "";
        for (int i = 0; i < cases.length; i++) {
            values = values + cases[i] + " ";
        }
        return values;
    }
    
    public int casesLeft() {
        Integer casesLeft = 0;
        for (Integer i = 1; i < cases.length; i++) {
            if (cases[i] != 0) {
                casesLeft += 1;
            }
        }
        return casesLeft;
    }
    
    public String[] remainingCases() {
        Integer remaining = casesLeft();
        String[] location = new String[remaining];
        Integer StringPosition = 0;
        for (Integer i = 1; i < cases.length; i++) {
            if (cases[i] != 0) {
                location[StringPosition] = i.toString();
                StringPosition = StringPosition + 1;
            }
        }
        return location;
    }
    
    public String valuesRemaining() {
        String values = "";
        for (Integer i = 1; i < remainingCases().length; i++) {
            if (cases[i] != 0) {
                values = values + cases[i] + "              ";                
            }
        }
        return values;
    }
    
    public void SwapCases(int A, int B) {
        int tempVar = cases[A];
        cases[A] = cases[B];
        cases[B] = tempVar;
    }
    
    public int location(int position) {
        String[] locations = remainingCases();
        String value = locations[position];
        int intvalue = Integer.parseInt(value.trim());
        return intvalue;
    }
    
    public int ValueOfLocation(int location) {
        Integer value = cases[location];
        return value;
    }
    
    public void findValue(int value) {
        for (int i = 1; i < cases.length; i++) {
            if (cases[i] == value) {
                cases[i] = 0;
                break;
            }            
        }
    }
    
    public void SetLocationto0(int location) {
        cases[location] = 0;
    }
    
    public double Median() {
        double median = 0.0;
        Integer middle1 = 0;
        Integer middle2 = 0;
        if (casesLeft() % 2 == 0 ) {
            // If number of items is even, take average of middle two numbers to find average
            middle1 = casesLeft() / 2;
            middle2 = middle1 - 1;
            median = (cases[middle2] + cases[middle1]) / 2;
        }
        else if (casesLeft() % 2 != 0) {
            middle1 = casesLeft() / 2;
            median = (cases[middle1]);
        }
        return median;
    }
    
    public int SumOfValue() {
        Integer sum = 0;
        for (int i = 0; i < cases.length; i++) {
            sum = sum + cases[i];
        }
        return sum;
    }
    
    public double Average() {
        int sum = SumOfValue();
        int items = casesLeft();
        int avg = sum / items;
        return avg;
    }
    
    public void Shuffle() {
        for (int i = 0; i < cases.length; i++) {
            int newLocation = (int)(Math.random() * (cases.length - 1) + 1);
            SwapCases(i,newLocation);
        }
    }
}
