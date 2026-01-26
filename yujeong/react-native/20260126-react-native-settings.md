React Native를 사용하기 위한 환경 설정을 진행합니다.
- os: mac os
- terminal: iterm

### 할 일
- [x]  node 설치
- [x]  안드로이드 스튜디오 설치
- [x]  xcode 설치
    

### 의존성 설치

- **Node & Watchman**

```bash
brew install node
brew install watchman
```

**✔️ brew install node**

→ 자바스크립트 실행 엔진

→ React Native는 자바스크립트로 앱을 만든다. 하지만 웹 브라우저가 아닌 터미널 환경에서 자바스크립트 코드를 해석하고, 필요한 라이브러리/패키지를 다운로드 하고, 앱을 빌드하는 모든 과정이 Node.js 위에서 돌아간다.

→ 함게 설치되는 것: `npm` (Node Package Manager), 이걸로 남들이 만들어 둔 좋은 라이브러리를 쉽게 가져다 쓸 수 있다.

**✔️ brew install watchman**

→ 파일 변경 감지 시스템 (Meta에서 만듦)

→ React Native의 장점 중 하나가 Fast Refresh (코드를 저장하면 앱 화면이 바로 바뀌는 기능) 이다.

프로젝트 내에는 수천 개의 파일이 존재한다. `watchman`이 없다면, 코드를 수정할 때마다 컴퓨터가 수천 개의 파일을 전부 뒤져서 무엇이 바뀌었는지 찾아야 하므로 매우 느려진다. 마치 CCTV처럼 파일들을 지켜보고 있다가, 변경된 파일만 콕 집어서 React Native에 알려준다. 그래서 성능 저하 없이 즉시 화면을 갱신할 수 있다.

```bash
node --version
# 결과 예시: v24.13.0
npm --version
# 결과 예시: 11.6.2
watchman --version
# 결과 예시: 2026.01.12.00
```

- JDK 설치

필자는 이미 깔려 있어서 생략했다. 방법은 아래와 같다.

```bash
brew install --cask zulu@17
```

JDK(Java Development Kit)

→ 자바 개발 도구 (안드로이드 앱을 만드는 공장)

→ React Native로 코딩은 자바스크립트로 하지만, 결국 안드로이드 폰에서 돌아가려면 안드로이드의 언어 (Java/Kotlin)로 변환되고 포장되어야 한다.

이 변환과 포장을 해주는 컴파일러가 JDK 안에 들어있다.

`zulu@17`은 Mac과 호환성이 가장 좋은 Java 배포판 버전이다.

```bash
javac -version
# 결과 예시: javac 17.0.9
echo $JAVA_HOME
# /Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
```

- 경로가 출력되지 않는다면?

다음과 같이 지정하거나, `vi ~/.zshrc` 로 직접 경로를 입력해줘도 된다.

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
source ~/.zshrc
```
<br>

### 안드로이드 개발 환경

- **Android Studio 설치**

Android Studio는 아래에서 다운받으면 된다. 필자는 homebrew를 이용해서 받았다.

https://developer.android.com/studio?hl=ko

```bash
brew install --cask android-studio
```

다운이 완료되면, Android Studio 앱 열고, 설정 마법사 시작

1. `Do not import settings`
2. `Standard`
3. `android-sdk-license` → `Accept`
4. `Finish` → Android SDK 다운 시작 (좀 걸림)

- `Android SDK Location`을 터미널에 등록해주기

```bash
vi ~/.zshrc
$ ANDROID_HOME=$HOME/Library/Android/sdk
$ PATH=$PATH:$ANDROID_HOME/emulator
$ PATH=$PATH:$ANDROID_HOME/platform-tools
$ PATH=$PATH:$ANDROID_HOME/tools
$ PATH=$PATH:$ANDROID_HOME/tools/bin
source ~/.zshrc
```

```bash
adb --version
# 결과 예시: 
Android Debug Bridge version 1.0.41
Version 36.0.2-14143358
Installed as /Users/yujeongee/Library/Android/sdk/platform-tools/adb
Running on Darwin 25.2.0 (arm64)
```

<br>

### React Native project 만들기

```bash
npx react-native init <yourAppName>
```

`package.json` 의 scripts 부분을 보면 설정된 것을 확인할 수 있다.

![](https://velog.velcdn.com/images/jjungyu12/post/dd27f438-5442-4e61-b9ca-fa3f8bfda8b6/image.png)


```bash
$ yarn <script name>
```

yarn을 통해 실행할 수 있다.

<br>

### Android 환경에서 React Native 앱 구동하기

Android Studio에서 만든 App > android 폴더를 열어 준다.

AVD Manager 열기 → Create Virtual Device → 기기 선택 → Finish

emulator가 구동됐으면, 만든 프로젝트의 디렉토리에서 작동해 보면 된다.

```bash
yarn android
```

![](https://velog.velcdn.com/images/jjungyu12/post/e6d0f2b0-a589-4343-bfa3-a84829828a80/image.png)


이런식으로 잘 뜨는 걸 확인할 수 있다.

<br>

### iOS 환경에서 React Native 앱 구동하기

- **Xcode와 CocoaPods 설치**

Xcode는 App Store에서 검색해서 설치한다.

```bash
brew install cocoapods
pod --version
# 결과 예시: 1.16.2
```

**Xcode**

애플이 만든 IDE다. 코드를 쓰고 컴파일하고 앱을 시뮬레이터나 실제 아이폰에 설치하는 과정을 담당한다.

**CocoaPods**

iOS용 의존성 관리 도구이다. Node.js의 `npm`이나 `yarn`과 같은 역할을 하지만, 대상이 iOS 네이티브 코드라는 점이 다르다. 외부 라이브러리를 내 프로젝트에 자동으로 다운로드하고 설치해준다.

`Podfile` 에 필요한 거 작성 → terminal에서 `pod install` 실행 → CocoaPods가 관련 코드들을 가져와서 내 프로젝트에 합쳐 줌

**CocoaPods 에러**가 떴다.

```
error Unable to open base configuration reference file '/Users/yujeongee/study-develop/react-native/MyApp/ios/Pods/Target Support Files/Pods-MyApp/Pods-MyApp.debug.xcconfig'. (in target 'MyApp' from project 'MyApp')
```

iOS용 라이브러리 설치가 안 되어 있어서 Xcode가 빌드 설정을 못 읽겠다는 의미다.

**해결 방법**

```bash
# 1. ios 디렉토리로 이동
cd ios
# 2. Pod 설치 명렁어 입력
pod install
```

![](https://velog.velcdn.com/images/jjungyu12/post/46023f30-03a0-48fe-b7ca-7c4df01437fc/image.png)



> **🙋시뮬레이터를 끄고 매번 재구동 시켜야 하나?**
Nooooooo!
에뮬레이터나 시뮬레이터를 새로 부팅하는 데 시간이 꽤 걸린다. 이미 떠있으면 `yarn ios` 명령어가 이를 감지하고 부팅 과정 없이 바로 앱 빌드와 설치 단계로 넘어가기 때문에 훨씬 빠르다.

> **🙋 매번 `yarn ios`를 입력할 필요가 없다!**
리액트 네이티브의 큰 장점은 Fast Refresh이다.
App.js나 App.tsx 등 파일을 수정하고 저장하면, 시뮬레이터가 알아서 바뀐 내용을 반영한다. 그래서 다시 빌드할 필요가 없다.

> ** 🙋 만약, 자동으로 반영이 안되면?**
시뮬레이터에서 `Cmd + R` 을 누르면 새로고침 된다.

> **🚨 주의!**
아래의 터미널이 Metro Bundler 라는 것이다.
우리가 작성한 여러 개의 코드 파일을 하나로 뭉쳐서 스마트폰이 이해할 수 있는 형태로 변환해 실시간으로 전송해 주는 역할을 한다.
이 터미널을 끄면, 앱 연결이 끊긴다.

![](https://velog.velcdn.com/images/jjungyu12/post/bee41673-ca9c-42c6-8392-947f61809042/image.png)


> ** 🙋 git이 자동으로 생겼다. **
모바일 프레임워크는 프로젝트를 생성할 떄 자동으로 `git init` 명령어를 실행하도록 설계되어 있다고 한다.
`node_modules`, `ios/Pods`, `build` 같이 용량이 엄청 큰 파일들은 `.gitignore`에 작성되어 있으니까 절대 지우면 안된다.
> 

### 문서

솔직히 공식문서만 보고 따라하기에는 매우 빈약하다고 느꼈다,,

[Set Up Your Environment-macOS-Android](https://reactnative.dev/docs/set-up-your-environment?platform=android)

[Set Up Your Environment-macOS-iOS](https://reactnative.dev/docs/set-up-your-environment?platform=ios)

[리액트 네이티브를 다루는 기술](https://product.kyobobook.co.kr/detail/S000001834713)

(Gemini와 Claude의 도움으로 환경설정한 과정입니다.)