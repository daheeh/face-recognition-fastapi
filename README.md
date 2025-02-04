# 얼굴 인식 출입 통제 시스템
**FastAPI**와 **InsightFace**를 활용한 **웹캠 기반 얼굴 인식 출입 통제 시스템**입니다  
AI 모델의 추론 과정을 이해하고 적용해보기 위한 목적으로 진행하였습니다

<br>

## 개발 기간
* 23.11.24 - 11.25 (2일)

<br>

## 개발 환경
  - `Python`
  - **IDE** : VSCode
  - **Framework** : FastAPI, Uvicorn
  - **Database** : MySQL
  - **ORM** : SQLAlchemy

<br>

## 기능 동작 설명
1. **실시간 웹캠 스트리밍**  
OpenCV를 사용해 웹캠에서 프레임을 캡펴하고 FastAPI의 StreamingResponse를 통해  
실시간으로 스트리밍하는 방식으로 구현하였습니다  
<br>

2. **얼굴 감지 및 임베딩 추출**  
  InsightFace의 face.get()메서드를 통해 얼굴을 감지하고, 임베딩을 추출합니다  
<br>

3. **얼굴 비교 후 출입 통제**  
   NumPy를 사용해 두 얼굴의 임베딩을 비교하고, 0.6 이상일 경우 출입을 허용하도록 하였습니다
