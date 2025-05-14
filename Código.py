import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

dedo_nomes = ['Polegar', 'Indicador', 'Medio', 'Anelar', 'Minimo']
dedo_ids = [4, 8, 12, 16, 20]

quadrados_dedos = []

dedo_selecionado = ""

def clique_mouse(event, x, y, flags, param):
    global dedo_selecionado
    if event == cv2.EVENT_LBUTTONDOWN:
        for idx, (qx, qy, qw, qh) in enumerate(quadrados_dedos):
            if qx < x < qx + qw and qy < y < qy + qh:
                dedo_selecionado = f"Voce clicou no dedo: {dedo_nomes[idx]}"

cv2.namedWindow("Reconhecimento de Mao")
cv2.setMouseCallback("Reconhecimento de Mao", clique_mouse)

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        break

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)
    image_height, image_width = image.shape[:2]
    quadrados_dedos = []

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for idx, id_ponto in enumerate(dedo_ids):
                x = int(hand_landmarks.landmark[id_ponto].x * image_width)
                y = int(hand_landmarks.landmark[id_ponto].y * image_height)

                
                tamanho = 40
                cor = (0, 255, 0)

                
                cv2.rectangle(image, (x - tamanho//2, y - tamanho//2),
                              (x + tamanho//2, y + tamanho//2), cor, 2)
                cv2.putText(image, str(idx+1), (x - 10, y + 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor, 2)

                
                quadrados_dedos.append((x - tamanho//2, y - tamanho//2, tamanho, tamanho))

    
    if dedo_selecionado:
        cv2.putText(image, dedo_selecionado, (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Reconhecimento de Mao", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
