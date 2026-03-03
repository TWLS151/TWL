# TXT-IMG 모델 활용법


모델 활용법에 대해서 배우고 있습니다.

모든걸 프롬프트로 작성해야해서 작가 같이 되어야 하는건가 했는데 여기에도 은근히 개발자 같이 프롬프트를 짤 수 있다는 점에서 놀라웠습니다.


일단 인물 변수에다가 인물의 설명을 적어두고, 프롬프트에 입력시 그 이름의 변수를 조회해서 설명을 통채로 집어 넣으니 일관성이 유지 되더군요.


그래서 이렇게 좀 재미없는? 방법으로 일단 일관성을 유지하고 있습니다.


그리고 이렇게 인물의 설정을 완전히 다르게 하니, 제각기 다른 인물들의 얼굴을 분류해서 잡아내는 것도 가능했습니다.


결과를... 보여드리고 싶지만....


비밀 비밀 프로젝트라서 오늘은 일단 이렇게 배운것만 올려두도록 하겠습니다.


감사합니다!!
# Face Feature Extraction Models Summary

| 모델 | 출력 타입 | 임베딩 차원 | 주요 라벨 / 필드 | 예시 출력 (1줄) |
|------|------------|-------------|------------------|------------------|
| SCRFD | bbox(+score), (옵션) keypoints | 미지정 | `bboxes[N,5]`, `kps[N,K,2]` (모델별 상이) | face#0: bbox=[x1,y1,x2,y2], score=0.99 |
| RetinaFace | bbox + 5 landmarks (+옵션 3D) | 미지정 | WIDER FACE 기반, 5 랜드마크 추가 | face#0: bbox=…, landmarks(5)=… |
| MTCNN | bbox + 5 landmarks | 미지정 | 3-stage cascade, landmark location 포함 | face#0: bbox=…, landmarks(5)=… |
| InsightFace (ArcFace 포함) | embedding + bbox / landmarks 등 | 미지정 (코드 확인) | 패키지/모델 구성별 상이, 상업 사용 시 라이선스 확인 필요 | embedding dim=…, 얼굴 1개 검출 |
| FaceNet (facenet-pytorch) | embedding | 512 (모델별 상이) | 512 latent embedding | embedding[512] 추출 완료 |
| AdaFace (IR50 MS1MV2) | embedding (`out = model(x)`) | 미지정 (코드 확인) | 입력: RGB, Normalize(0.5,0.5,0.5), 112×112 | AdaFace embedding shape=(1, D) |
| DeepFace | dict(속성) + (옵션) embedding | 백엔드별 상이 | age, gender, emotion(angry/fear/.../surprise), race(asian/white/...) | age=27, gender=Woman, emotion=happy, race=asian |
| FairFace | 분류 결과 + score 벡터 | N/A | race_7=[White, Black, Latino_Hispanic, East, Southeast Asian, Indian, Middle Eastern], gender=[Male,Female], age=[0-2,3-9,...,70+] | race=East, gender=Female, age=20-29 |
| Age-Gender ViT (onnx-community) | dict(age, gender, confidence) | N/A | age(0–100), gender(Male/Female), gender_confidence | 25 years, Female (87.3% confidence) |
| face-alignment (FAN) | landmarks | N/A | 2D/3D 랜드마크 (보통 68점) | landmarks shape=(68,2) |
| Face Parsing (SegFormer) | segmentation mask (H×W) | N/A | id2label에 부위 라벨 정의 (skin, nose, hair 등) | mask shape=(H,W), unique labels={...} |
| Face Parsing (BiSeNet) | segmentation mask (H×W) | N/A | 눈/코/입/윤곽 등 얼굴 부위 분할 | mask shape=(H,W) |

