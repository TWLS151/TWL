# Access Modifier

---

은행 어플을 사용하는데 내가 내 계좌의 잔액을 마음대로 변경할 수 있다면 어떻게 될까?  

말도 안되는 일이 일어나게 될 것이고 이는 아주 심각한 버그이다.  

이런 상황을 막아주는 것이 접근 제어자이다.  
`private`, `default`, `protected`, `public` 총 네 가지가 있으며 모두 다 기능이 다르다.
1. `private`
    - 모든 외부 호출을 막는 접근 제어자이다.
2. `default`
   - 같은 패키지 안에서의 호출까지 허용한다.
3. `protected`
   - 같은 패키지 안에서의 호출을 허용하고, 패키지가 달라도 상속관계의 호출까지 허용한다.
4. `public`
    - 모든 외부 호출을 허용한다.

```java
package access.a;

public class AccessData {
    
    public int publicField;
    int defaultField;
    private int privateField;
    
    public void publicMethod() {
    }
    
    void defaultMethod() {
        
    }
    
    private void privateMethod() {
        
    }
    
    public void innerAccess() {
        publicField = 100;
        defaultField = 200;
        privateField = 300;
        publicMethod();
        defaultMethod();
        privateMethod();
    }
}
```
이렇게 클래스를 생성하면 `public`은 어떤 곳에서든 접근이 가능하고 `private`은 public 메서드인 `innerAccess()`를 통해서만 접근이 가능하다.
  
은행 어플에서 내가 내 잔액을 직접 건드리지 못하고 송금, 출금, 입금 등 특정 방법만으로 접근할 수 있게 하는 것과 같다.


# ***Encapsulation, 캡슐화***

---

캡슐화는 OOP에서 상당히 중요한 개념 중 하나로 데이터와 데이터 처리 메서드를 하나로 묶어 외부에서의 접근을 제한하는 것을 말한다.
캡슐화를 통해 데이터의 직접적 변경을 방지하거나 제한할 수 있다.
  
외부에는 필요한 기능만 노출하고 다른 모든 데이터나 기능은 내부로 숨기는 것이다.

그럼 어떤걸 노출하고 어떤걸 숨겨야할까?

1. 데이터   
    우선 데이터를 숨겨야한다.  
    객체에는 속성과 기능이 있는데 가장 우선적으로 숨겨야하는 건 속성이다. 위에서 들었던 은행계좌 예시와 같은 맥락이다.  
    **객체의 데이터는 객체가 제공하는 메서드를 통해서만 접근할 수 있어야한다.**

2. 메서드  
    메서드는 모든 메서드를 숨겨야하는 건 아니고 내부에서만 사용되는 메서드를 숨겨야한다.  
    송금이나 입금을 할 때 어떤 원리로 입금이 되고 송금이 되는지까지 사용자가 알아야할 필요는 없다. 그냥 버튼을 누르면
    입금이 되고 송금이 되는 것이다.  
    이러한 원리는 숨기고, 버튼만 외부에 노출 시켜야한다.

다음은 이상적인 캡슐화 코드이다.
```java
package access;

public class BankAccount {
    
    private int balance;
    
    public BankAccount() {
        balance = 0;
    }
    
    public void deposit(int amount) {
        if (isAmountValid(amount)) {
            balance += amount;
        } else {
            System.out.println("유효하지 않은 금액");
        }
    }
    
    public void withdraw(int amount) {
        if (isAmountValid(amount) && balance - amount >= 0) {
            balance -= amount;
        } else {
            System.out.println("유효하지 않은 금액");
        }
    }
    
    public int getBalance() {
        return balance;
    }
    
    private boolean isAmountValid(int amount) {
        return amount > 0;
    }
}
```
계좌 잔액은 숨기고 입금, 출금, 잔액확인 버튼만 노출시켰으며 입출금의 트리거가 되는 검증 메서드도 숨겼다.  
잔액을 변경하기 위해 할 수 있는 건 입금, 출금 버튼을 건드리는 것 밖에 없다.  
필요한 메서드만 노출시키고 데이터와 노출할 필요가 없는 메서드는 숨겼다.  

이 코드는 아니지만 예제 문제를 해결하며 물건의 총 금액을 구하는 기능 구현에서 잠깐 해메었는데,
수량과 가격을 곱해 총액을 출력해야했다.   

위 코드의 `getBalance` 메서드처럼 데이터에 접근하는 메서드를 생성해서 값을 구한 뒤 출력했어야했는데
미처 생각하지 못해서 결국 데이터의 `private` 속성을 지우고 구현했는데 기능은 구현했지만 명세에 맞추지 못해서 많이 아쉬웠다.