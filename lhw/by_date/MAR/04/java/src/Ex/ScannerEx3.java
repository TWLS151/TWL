package Ex;

import java.util.Scanner;

public class ScannerEx3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("음식 이름을 입력해주세요:");
        String foodname = scanner.nextLine();

        System.out.print("음식의 가격을 입력해주세요:");
        int foodprice = scanner.nextInt();

        System.out.print("음식의 수량을 입력해주세요:");
        int foodquantity = scanner.nextInt();

        System.out.println(foodname + " " + foodquantity + "개를 주문하셨습니다." +
                " 총 가격은 " + foodprice*foodquantity + "원입니다.");
    }
}
