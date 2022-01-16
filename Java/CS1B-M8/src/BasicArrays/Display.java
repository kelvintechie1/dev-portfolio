package BasicArrays;
public class Display {

    public static void display(int[] Array) {
        String FinalString = "";
        Integer arrayLength = Array.length;
        for (int i = 0; i < arrayLength; i++) {
            FinalString = FinalString + Array[i] + " ";
        }
        System.out.println(FinalString);
        
    }
    public static void main(String[] args) {
        int[] TestArray = {15,29,133,54,24,100,14,24,19,25,122,199,1451,154};
        display(TestArray);
    }
    
}
