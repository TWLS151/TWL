# ***STATIC***

스태틱을 설명하기 위해서는 자바의 메모리 구조를 이해해야한다.
  
자바의 메모리는 크게 메서드 영역. 스택 영역, 힙 영역으로 나뉘고 그 특징을 간단히 나열하면 다음과 같다.
- 메서드 영역: 클래스 정보를 보관한다. ( 붕어빵 틀 )
- 스택 영역: 실제 프로그램이 실행되는 영역이다. 메서드를 실행할 때 마다 하나씩 쌓인다.
- 힙 영역: 객체가 생성되는 영역이다. `new` 명령어를 통해 생성하는 객체가 이 영역을 사용한다. ( 만들어진 붕어빵 )

  
- 상세:
```angular2html
1. 메서드 영역: 프로그램을 실행하는 데 필요한 공통 데이터를 관리한다. 이 영역은 프로그램의 모든 영역에서 공유한다.
    - 클래스 정보: 클래스의 실행코드, 필드, 메서드와 생성자 코드 등 모든 실행코드가 존재한다.
    - Static 영역: PYHON의 클래스 변수, 메서드에 해당하는 Static 변수와 메서드를 관리하는 영역이다.
    - 런타임 상수 풀: 추후 추가 학습

2. 스택 영역: 자바 실행 시 하나의 실행 스택이 만들어지고 각 스택 프레임은 지역 변수, 중간 연산 결과, 메서드 호출 정보 등을 포함한다.
    ( 파이썬과 동일 )
    - 스택 프레임: 스택 영역에 쌓이는 하나의 스택을 이야기한다. ( 파이썬에서 재귀 스택 생각하기 )
    - 스택: 자료 구조 중 하나인 스택 개념을 채용하고 큐와 반대되는 후입선출 개념이다.

3. 힙 영역: 객체와 배열이 생성되는 영역이다. `GC`가 이루어지는 주요 영역이며 더 이상 참조되지 않는 객체는 GC에 의해 제거된다.
```

> 참고: 스택 영역은 쓰레드 개념이 추가로 존재하는데 스택 영역 그 자체를 이야기 한다고 생각하자. 지금은 쓰레드를 한 개만 사용하지만
> 추후 추가 학습을 통해 멀티 쓰레드 개념을 배울 예정

---

***정리***
스택 영역에서는 지역 변수가, 힙 영역에서는 객체가 관리된다. 남은 메서드 영역에서는 이제부터 설명할 `STATIC` 변수가 관리된다.

---
## STATIC


### STATIC VAR
  
드디어 주인공의 등장이다. 이 녀석을 설명하기 위해 위의 긴 설명들을 해야만 했다.
  
`static` 키워드는 주로 멤버 변수 ( python 의 클래스 변수 )와 메서드에 사용된다. 예시를 한 번 보자  
```java
// Data1
public class Data1 {
    public String name;
    public int count;
    
    public Data1(String name) {
        this.name = name;
        count++;
    }
}
```
```java
// DataCountMain1
public class DataCountMain1 {

    static void main() {
        Data1 data1 = new Data1("A");
        System.out.println("A count = " + data1.count);
        
        Data1 data2 = new Data1("B");
        System.out.println("B count = " + data2.count);
        
        Data1 data3 = new Data1("C");
        System.out.println("C count = " + data3.count);
    }
}
```
위 코드를 실행하면 의도대로 카운팅이 잘 될까?
인스턴스를 생성할 때마다 카운팅을 한 개씩 했으니 마지막에는 `count == 3`이어야 한다.
```
// 출력
A count = 1
B count = 1
C count = 1
```
잘못되었다. 왜 그런걸까?  

---

카운트를 인스턴스 변수로 만들었기 떄문이다. 인스턴스를 만들 때마다 각 인스턴스가 count 변수를 가지게 되는 것이다.
  
의도대로 글로벌 카운트를 구현하려면 여러가지 방법이 있을 수 있다. 뭐 메인 메서드에 변수를 하나 만들어도 가능하고 아니면  
추가 클래스를 하나 더 만들어서 다른 객체에서 변수를 관리해도 된다.  

하지만 가장 효과적인, 객체지향적인 방법은 `static`을 사용하는 것이다. `static`을 통해 해당 클래스 내부에서 글로벌 변수를 관리할 수 있게 된다.

```java
// 새 클래스
public class Data3 {
    public String name;
    public static int count;
    
    public Data3(String name) {
        this.name = name;
        count ++;
    }
}
```
`static` 이 선언된 변수는 클래스 변수 ( `정적 변수` or `static` ) 가 되어 인스턴스가 아닌 클래스 내부에서 관리된다.
  
그래서 외부에서 이 변수에 접근할 때 또한 클래스에 접근하는 것 처럼 (`Data3.count`) 해야한다.

### STATIC METHOD

다음으로 스태틱 메서드는 무엇일까?

먼저 말하자면 `static`이 선언된 메서드는 별도의 인스턴스 생성 및 호출 없이 클래스에 접근해 호출할 수 있다.
```java
public class DecoUtil2 {
    
    public static String deco(String str) {
        String result = "*" + str + "*";
        return result;
    }
}
```
이렇게 클래스를 선언하면 `DecoUtil2.deco(str)` 같은 접근이 가능해진다.

추가로 `import` 를 활용하면 클래스명도 없이 `deco(str)`만으로도 메서드 호출이 가능하다. 또한 다른 인스턴스 메서드와 같이
`instance.method()`로도 접근이 가능하다.

---

static 메서드를 사용할 때는 주의할 점이 몇가지 있는데 이는 다음과 같다.
- static 메서드는 static 만 사용할 수 있다.
  - 클래스 내부의 기능을 사용할 때, 정적 메서드는 정적 메서드나 정적 변수만 사용할 수 있다. ( 인스턴스 메서드, 변수 사용 불가 )
- 반대로 모든 곳에서 static을 호출할 수 있다.
  - 정적 메서드는 공용 기능이기 떄문에 접근 제어자만 허락한다면 클래스를 통해 모든 곳에서 static을 호출 할 수 있다.


---

> ***Main() 메서드는 정적 메서드이다.***  

인스턴스 없이 실행하는 가장 대표적 메서드낙 바로 메인 메서드인데 이는 프로그램을 시작하는 시작점이 된다.
  
정적 메서드이기 때문에 main() 메서드 또한 주의점을 따라야한다.
```java
public class ValueDataMain {
    
    public static void main(String[] args) {
        ValueData valueData = new ValueData();
        add(valueData);
    }
    
    static void add(ValueData valueData) {
        valueData.value++;
        System.out.println("숫자 증가 value=" + valueData.value);
    }
}   
```