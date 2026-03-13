# ***Package***

### ***12ND MAR***

프로그램 개발을 하다보면 클래스가 정말 많이 쌓이는데 이 많은 클래스를 분류해 관리하고 싶을 때 Directory 기능을 이용한다.  
자바에서는 `Directory` 기능을 `Package`로 제공한다.

---

패키지는 위치가 정말 중요한데 스코프 개념이 들어가기 때문이다.
```java
package pack;

public  class  Data {
    public Data() {
        System.out.println("패키지 pack Data 생성");
    }
}
```
위와 같이 pack 패키지에 Data 클래스를 만들었다.

```java
package pack.a;

public class User {
    
    public User() {
        System.out.println("패키지 pack.a 회원 생성");
    }
}
```
이번에는 pack 의 하위 패키지 a를 만들고 그 안에서 User 클래스를 만들었다.
이렇게 하면 상위 패키지 pack 에서 하위 패키지 a 안의 클래스 User를 사용할 수 있다.

```java
package pack;

public class PackageMain1 {
    static void main() {
        Data data = new Data();
        pack.a.User user = new pack.a.User();
    }
}
```
대신 파일의 위치를 적어주어야한다는 제약이 존재한다.  
이 위치를 안적을 수는 없을까?
```java
package pack;
import pack.a.User;
import pack.a.*;
```
이렇게 `import` 문을 사용하면 가능하다.  
그리고 두번째 import 같이 `*`을 import 해오면 pack.a 안의 모든 클래스를 사용할 수 있다.
  ---
```java
pack.a.User;
pack.b.User;
```
그럼 이렇게 이름이 같은 클래스는 어떻게 될까?
```java
import pack.a.User;

User userA = new User();
pack.b.User userB = new pack.b.User();
```
위와 같이 사용해야한다. 둘 다 생략할 수는 없고 둘 중 자주 사용하는 클래스를 import 해 생략하고
비교적 덜 사용하는 클래스를 불러 사용하는 것이 효율적일 것이다.

----

### 패키지의 계층 구조

- `a`
  - `b`
  - `c`

이 구조에는 총 3개의 패키지가 존재한다.
`a`, `a.b`, `a.c`  
그리고 이 세 패키지는 모두 전혀 다른 패키지이다.  
한 패키지에서 다른 패키지의 클래스를 사용하려면 반드시 `import`를 사용해야한다.