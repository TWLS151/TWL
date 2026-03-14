# 11ST MAR - TIL


### DataStructure
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

## **Null**

참조형 변수에 참조값이 아직 있지 않다는 것을 의미하고 변수를 참조형으로 초기화하기는 했으나 아직 참조값을 부여하지 않은 상태이다.

1. **GC** ( Garbage Collection )  
 그럼 참조값에 객체를 만든 후에 참조값만 지운다면 객체는 어떻게 될까?  
 **지워진다**  
 어떤 변수도 참조하지 않는 객체가 있다면 JVM 의 GC 가 더 이상 사용하지 않는 객체라고 판단해 인스턴스를 자동으로 메모리에서 제거한다.

2. **NullPointerException**  
    객체를 참조할 때, `dot`을 이용해 객체를 찾아간다. 그런데 이 때 참조하려는 참조값에 객체가 없다면 발생하는 에러이다.

```java
public class NullMain {
    public static void main(String[] args) {
        Data data = null;
        data.value = 10;
        System.out.println("data = " + data.value);
    }
}
```
위 코드는 에러가 발생하고 즉시 종료된다.  
`data == null` 인데 `data.value = 10;` 부분에서 참조를 하려하니 에러가 발생하며 그 아래로는 코드가 더 진행되지 않는다.
