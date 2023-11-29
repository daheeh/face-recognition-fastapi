
from fastapi import FastAPI, File, Request, UploadFile
import cv2
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from insightface.app import FaceAnalysis
import numpy as np
from models import Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

face = FaceAnalysis(providers=['CPUExecutionProvider'])
face.prepare(ctx_id=0, det_size=(640, 640))

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIRECTORY = "capture_img"

# html파일(템플릿) 파일 위치
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


# process_frame함수에서 프레임 처리하고 클라이언트로 스트리밍
def generate_frames():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face.get(frame)

        if faces:
            cv2.imwrite(f'{UPLOAD_DIRECTORY}/captured_frame.jpg', frame)
            # cap.release()
            continue

        # 웹캠에서 영상 프레임을 JPEG 포맷으로
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        # if faces:
        #     save_image_to_db(f'{UPLOAD_DIRECTORY}/captured_frame.jpg', frame)

        #변환된 프레임을 반환
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')


# 기본 화면
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 웹캠 송출
@app.get("/video")
def video():
    # 클라이언트로부터 스트리밍된 데이터를 반환
    return StreamingResponse(generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


# 캡쳐된 사진과 등록된 사진 비교
@app.post("/compare")
async def img_file():

    img1 = cv2.imread('capture_img/captured_frame.jpg')
    faces1 = face.get(img1)
    img2 = cv2.imread('user/kdw.jpg')
    faces2 = face.get(img2)

    feat1 = np.array(faces1[0].normed_embedding, dtype=np.float32)
    feats2 = np.array(faces2[0].normed_embedding, dtype=np.float32)

    sims = np.dot(feat1,feats2)

    if sims > 0.6:
        return 1
    else :
        return 0

 

# DB 테스트
 