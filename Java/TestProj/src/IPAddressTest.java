import java.lang.Object;
import java.net.Inet4Address;
import java.net.UnknownHostException;

public class IPAddressTest {

    public static void main(String[] args) throws UnknownHostException {
        byte[] ipadd = new byte[]{(byte) 224, 0, 0, 10};
        Inet4Address ip = (Inet4Address) Inet4Address.getByAddress(ipadd);
        System.out.println("IP is multicast: " + ip.isMulticastAddress());
    }
}
