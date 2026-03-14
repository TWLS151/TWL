# 10TH MAR - TIL  

### JAVA
1. Class
    - 클래스의 개념은 파이썬과 크게 다르지 않다. 하위 클래스, 객체를 포함하는
   상위 클래스를 만들고 인스턴스 변수와 클래스 변수를 활용해 데이터를 효과적으로 관리한다.
   같은 종류의 데이터를 관리하기 위해 객체마다 새로운 변수를 초기화 할 필요가 없어진다.
    - 쉽게 표현하자면 `int` or `String` 같은 타입을 만든다고 볼 수 있다.  
   타입을 만들기 위한 `설계도`가 클래스이고 설계도를 활용해 실제 메모리에 만들어진 실체를 `객체` 또는 `인스턴스`라 부른다.
   ```java
   // Student Class 선언
   public class Student {
        Stirng name;
        int age;
        int grade;
   }
   // 새로운 클래스인 Student를 선언했고 Student의 클래스 변수는
   // name, age, grade 총 세 가지가 있다.
    ```
   
   ```java
   public class Class {
        public static void main(Stirng[] args) {
            Student student1 = new Student();
            student1.name = "학생1";
            student1.age = 15;
            student1.grade = 90;
        }
   }
   ```
   - 위의 박스는 클래스를 생성한 부분이고 아래의 박스는 그 선언한 클래스의 객체를 만든 부분이다.  
   이렇게 클래스의 인스턴스를 만들면 이 인스턴스 변수 `student1` 은 어떤 값을 갖는게 아니라
   객체가 담겨있는 메모리의 **참조값**을 갖는다.  
   객체의 정보 출력을 시도하게 되면 변수에 담겨있는 정보가 출력되는게 아니라 변수가 갖고 있는
   메모리 주소를 참조하여 해당 메모리로 이동한 뒤 그 메모리의 정보를 출력한다.
     - 이 부분은 파이썬과도 일맥상통하는 부분인데 항상 궁금헀던 '함수 스코프 밖에 있는 해셔블 데이터를
     어떻게 참조하는 지'에 대한 부분이 해결되었다. 참조값을 갖기 때문에 참조값을 갖지 않는 기본형 데이터들은 스코프에
     묶이고 참조값을 갖는 데이터는 스코프에 묶이지 않는 것으로 이해했다.
     - 여러모로 참 도움 되는 자바 공부라는 생각이 들었다.

```java
package Class.Ex1;

public class MovieReviewMain2 {

    public static void main(String[] args) {
        MovieReview inception = new MovieReview();

        inception.title = "인셉션";
        inception.review = "it was good";

        MovieReview abouttime = new MovieReview();

        abouttime.title = "어바웃타임";
        abouttime.review = "good too";

        MovieReview[] movies = new MovieReview[2];
        movies[0] = inception;
        movies[1] = abouttime;

        for (MovieReview movie : movies) {
            MovieReview m = movie;
            System.out.println(m.review + " " +  m.title);
        }

    }
}
```
```java
package Class.Ex1;

public class ProductOrderMain1 {

    public static void main(String[] args) {
        ProductOrder[] products = new ProductOrder[3];

        ProductOrder product1 = new ProductOrder();
        product1.productName = "두부";
        product1.price = 2000;
        product1.quantity = 2;
        products[0] = product1;

        ProductOrder product2 = new ProductOrder();
        product2.productName = "김치";
        product2.price = 5000;
        product2.quantity = 1;
        products[1] = product2;

        ProductOrder product3 = new ProductOrder();
        product3.productName = "콜라";
        product3.price = 1500;
        product3.quantity = 2;
        products[2] = product3;

        int total = 0;

        for (ProductOrder product : products) {
            System.out.println("상품명: " + product.productName + ", 가격: " + product.price + ", 수량: " + product.quantity);
            total += product.price * product.quantity;
        }

        System.out.println("총 결제 금액: " + total);
    }
}
```
간단한 문제 풀이 두 개.

추후에는 두번째 문제의 객체 생성 부분도 최적화하는게 가능하다고 한다.
    

2. DataStructure(..?)
   1. 기본형 vs 참조형 데이터
      - 기본형 : `int`, `long`, `double`, `boolean` 같이 변수에 값을 직접 넣는 데이터 타입
      - 참조형 : `Student student1`, `int[] student` 같이 데이터에 접근하기 위한 참조를 저장하는 데이터 타입 
      - `String` : String은 사실 클래스라서 참조형 데이터인데 문자열은 매우 자주 다루는 데이터 타입이기 때문에
                특별하게 편의 기능을 제공받는다.
   
   2. 기본형 vs 참조형 변수 대입
        > 자바는 항상 변수의 값을 복사해서 대입한다.
      - 기본형은 변수의 값을 직접 복사해서 대입하지만 참조형은 데이터 주소를 복사해서 대입하기 때문에
        주의해야한다.
        ```python
        # 파이썬에서 아래와 같이 리스트를 생성하면 안되는 이유와 같다.
        student1 = student2 = []
        ```
        위와 같이 리스트 두 개를 만들게 되면 같은 해시를 공유하기 때문에 `student1` 을 통해 변화를 주면
        `student2` 도 영향을 받았던 기억이 있다. 사실 영향을 받는 게 아니라 같은 주소를 사용하기 때문에 그렇게 보인다는 사실을 이해했다.
   
   3. 메서드 호출
   ```java
    public class MethodChange {
        public static void main(String[] args){
          int a = 10;
          System.out.println(a);
          changeMethod(a);
          System.out.println(a);
        }
        static void changeMethod(int x) {
            x = 20;
       }    
   }
    ```
    위 코드의 결과는 변수 `a`가 기본형이기 때문에 메서드 내부에서 값이 변화해도
    리턴값을 받지 않는 이상 `a`에는 아무런 영향을 끼치지 못한다.

    ```java
    public class MethodChange {
        static void main(){
          Data dataA = new Data();
          dataA.value = 10;
          System.out.println(dataA.value);
          changeMethod(dataA);
          System.out.println(dataA.value);
        }
        static void changeMethod(Data dataX) {
            dataX.value = 20;
       }
   }
    ```
    그럼 이 코드는 어떤가? `Data`라는 클래스의 인스턴스인 `dataA`는 지금 어떤 값을 갖는게 아니라
    `객체 dataA`의 참조값만을 가지고 있다. 그래서 메서드의 인수로 dataA를 넣으면 참조값이 들어가게 되고
    참조값을 통해 해당 객체에 변화를 주게 되면 당연히 메서드 밖에서도 영향을 받게 되는 것이다.

자바 재밌다.