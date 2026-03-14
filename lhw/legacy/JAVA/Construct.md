# **Construct, 생성자**

### ***12ND MAR***
---

1. Constuctor
    - 객체를 만들며 동시에 데이터 초기값을 설정하게 한다. 파이썬의 `__init__`
```java
public class MemberInit {
   String name;
   int age;
   int grade;
}
```
위와 같이 클래스를 만들면 메인 클래스에서 다음과 같이 값을 부여해야한다.
```java
void main() {
   //객체를 만들고
   MemberInit member1 = new MemberInit();
   //값을 초기화한다.
   member1.name = "user1";
   member1.age = 15;
   member1.grade = 90;
}
```
객체가 한 개라서 별 무리없이 진행했지만 객체가 많아진다면 무의미한 반복 코드가 많아진다.
그래서 다음과 같이 생성자 메서드를 직접 정의한다.
```java
public class MemberInit {
    String name;
    int age;
    int grade;
    
    MemberInit(String name, int age, int grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }
}
```
이렇게 생성자 메서드를 정의하게 되면 ( 클래스 파일에 생성자 메서드가 없다면 자바에서 기본적으로 아무것도 없는 기본 생성자 메서드를 제공한다. )
인스턴스를 만들 때 조금 더 편하게 ( 반복 없이 ) 생성이 가능하다.
```java
void main() {
   MemberInit member1 = new MemberInit("user1", 15, 90);
}
```
위와 같이 인스턴스 생성과 동시에 초기값을 부여한다. 주의할 점은 생성자 메서드의 이름은 항상 클래스 명과 같아야한다는 점이다.
  
또한 생성자를 하나 이상 정의했다면 기본 생성자가 제공되지 않으니 새로 정의한 생성자를 반드시 이용해야한다.  

- 생성자는 오버로딩 또한 가능하다.

```java
// this()를 사용한 오버로딩 예시

public class MemberConstruct {
    String name;
    int age;
    int grade;
    
    MemberConstruct(String name, int age) {
        this(name, age, 50);
    }
    
    MemberConstruct(String name, int age, int grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }
}
```
첫 번째 생성자는 `this()`를 활용해 두 번째 생성자를 호출한다.  
`Init(String name, int age) -> Init(String name, int age, int grade)`  
`this()` `name`, `age`, `50` 이 인자로 들어간다.