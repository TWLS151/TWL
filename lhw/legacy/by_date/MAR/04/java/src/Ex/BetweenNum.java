package Ex;

import java.util.Scanner;

public class BetweenNum {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("첫 번째 숫자를 입력하세요:");
        int num1 = input.nextInt();

        System.out.print("두 번째 숫자를 입력하세요:");
        int num2 = input.nextInt();

        int base;
        if (num1 > num2) {
            base = num2;
            num2 = num1;
            num1 = base;
        }

        System.out.print("두 숫자 사이의 모든 정수:");
        for (int i = num1; (i <= num2);i++) {
            System.out.print(i);
            if (i != num2) {
                System.out.print(", ");

            }
        }
    }
}
