
class Car {
    public static void main( String[] args ) {}
    int milesDriven;
    int oilChangeDuration;

    int lastOilChangeMileage;

    public Car(int milesDriven, int oilChangeDuration) {
        this.milesDriven = milesDriven;
        this.oilChangeDuration = oilChangeDuration;

        // 0 reports that oil was never chnaged
        this.lastOilChangeMileage = 0;
    }

    public boolean timeForOilChange() {
        if (milesDriven - lastOilChangeMileage > oilChangeDuration) {
            // Since it is time to change oil we set the last oil change to the current
            // miles driven
            lastOilChangeMileage = milesDriven;
            return true;

        } else {
            return false;
        }
    }

    public void addMiles(int miles) {
        milesDriven += miles;
    }
}

public class KennyThing {
    public static void main(String[] args) {
        Car c = new Car(9000,3000);
        System.out.println(c.timeForOilChange());

        c.addMiles(2000);
        System.out.println(c.timeForOilChange());

        c.addMiles(2000);
        System.out.println(c.timeForOilChange());
    }
}
