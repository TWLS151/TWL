package loop;

public class pro1 {

    public static void main(String[] args) {
        int count = 1;
        while (count <= 10) {
            System.out.println(count);
            count += 1;
        }
        count = 1;
        for (; ; ) {
            if (count > 10) {
                break;
            }
            System.out.println(count);
            count += 1;
        }
        for (int counat = 1; counat <= 10; counat++) {
            System.out.println(counat);
        }
    }
}
