# 11TH MAR - TIL

### **OOP**, 객체지향 프로그래밍
1. 절차지향과 객체지향  
    1. `절차지향`은 프로그램의 실행 순서를 중요하게 생각하는 방식으로 코드의 흐름을 순서대로 따라간다.
        - "어떻게"를 중심으로 프로그래밍을 한다.
    2. `객체지향`은 객체들 간의 상호작용을 중심으로 프로그래밍을 하는 방식이다.
        - "무엇을"을 중심으로 프로그래밍을 한다.
    - **절차지향**은 데이터와 데이터에 대한 처리 방식이 분리되어 있지만 **객체지향**은 데이터와 그 데이터 처리 방식이 한 객체 안에 포함되어있다.

    > 지금까지 파이썬을 사용한 방식은 절차지향이고 지금 자바를 사용하는 방식인 클래스를 활용하는 방식은 객체지향이다.

> 목표 출력
```
음악 플레이어를 시작합니다.
음악 플레이어 볼륨:1
음악 플레이어 볼륨:2
음악 플레이어 볼륨:1
음악 플레이어 상태 확인
음악 플레이어 ON, 볼륨: 1
음악 플레이어를 종료합니다.
```

> 최적화된 절차지향 코드
```java
public class MusicPlayerMain3 {

    public static void main(String[] args) {
        MusicPlayerData data = new MusicPlayerData();

        on(data);

        volumeUp(data);
        volumeUp(data);
        volumeDown(data);
        showStatus(data);

        off(data);
    }

    static void on(MusicPlayerData data) {
        data.isOn = true;
        System.out.println("음악 플레이어를 시작합니다.");
    }

    static void off(MusicPlayerData data) {
        data.isOn = false;
        System.out.println("음악 플레이어를 종료합니다.");
    }

    static void volumeUp(MusicPlayerData data) {
        data.volume ++;
        System.out.println("음악 플레이어 볼륨:" + data.volume);
    }

    static void volumeDown(MusicPlayerData data) {
        data.volume --;
        System.out.println("음악 플레이어 볼륨:" + data.volume);
    }

    static void showStatus(MusicPlayerData data) {
        System.out.println("음악 플레이어 상태 확인");
        if (data.isOn) {
            System.out.println("음악 플레이어 ON, 볼륨: " + data.volume);
        } else {
            System.out.println("음악 플레이어 OFF");
        }
    }
```
> 절차지향 클래스 파일
```java
public class MusicPlayerData {
    int volume = 0;
    boolean isOn = false;
}
```

> 객체지향 코드
```java
public class MusicPlayerMain4 {

    public static void main(String[] args) {
        MusicPlayer player = new MusicPlayer();

        player.on();
        player.volumeUp();
        player.volumeUp();
        player.volumeDown();
        player.showStatus();
        player.off();
    }
}
```
> 객체지향 클래스 파일
```java
public class MusicPlayer {

    int volume = 0;
    boolean isOn = false;

    void on() {
        isOn = true;
        System.out.println("음악 플레이어를 시작합니다.");
    }

    void off() {
        isOn = false;
        System.out.println("음악 플레이어를 종료합니다.");
    }

    void volumeUp() {
        volume ++;
        System.out.println("음악 플레이어 볼륨:" + volume);
    }

    void volumeDown() {
        volume --;
        System.out.println("음악 플레이어 볼륨:" + volume);
    }

    void showStatus() {
        System.out.println("음악 플레이어 상태 확인");
        if (isOn) {
            System.out.println("음악 플레이어 ON, 볼륨: " + volume);
        } else {
            System.out.println("음악 플레이어 OFF");
        }
    }
```

두 방식 모두 다 출력은 정상적으로 나온다.  
차이는 데이터와 데이터 처리 방식이 분리되어 있는지, 아니면 하나로 묶여있는지의 차이이다.

--------
절차지향 코드를 보면 데이터는 클래스 파일에 존재하는데 메서드는 메인 파일에 존재해서 데이터를 수정하게 되면 메인 파일에서 메서드 또한 수정해야한다.  
하지만 객체지향은 클래스 파일 안에서 수정을 마치면 메인 파일에서 따로 수정할 필요가 없다.  


지금은 간단한 코드를 작성하는 법만 배웠지만 추후 더 깊게 이해해야하는 주제인 것 같다.