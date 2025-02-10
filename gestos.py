import cv2
import mediapipe as mp

# Inicializar MediaPipe e OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Função para identificar gestos
def reconhecer_gesto(landmarks):
    """
    Reconhece gestos de "👍" (legal) e "👌" (ok).

    Parâmetros:
    - landmarks: Lista de coordenadas normalizadas (x, y, z) dos pontos de referência da mão.

    Retorna:
    - Uma string descrevendo o gesto reconhecido ou "Gesto não identificado".
    """
    x_polegar, y_polegar = landmarks[4][0:2]  # Dedo polegar (dedo 4)
    x_palma, y_palma = landmarks[0][0:2]  # Centro da palma (dedo 0)

    # Coordenadas para "👌"
    x_indicador, y_indicador = landmarks[8][0:2]  # Dedo indicador (dedo 8)
    x_medio, y_medio = landmarks[12][0:2]  # Dedo médio (dedo 12)

    # Detectar gesto "👍" (polegar para cima)
    polegar_cima = (
        y_polegar < y_palma and  # Polegar acima da palma
        landmarks[3][1] < y_polegar and  # Junta do polegar abaixo da ponta
        all(landmarks[i][1] > y_palma for i in [6, 10, 14, 18])  # Outros dedos abaixo da palma
    )

    # Detectar gesto "👌" (indicador e polegar formando um círculo)
    ok_gesto = (
        abs(x_polegar - x_indicador) < 0.1 and  # Polegar e indicador próximos (distância menor que 0.1)
        abs(y_polegar - y_indicador) < 0.1 and  # Polegar e indicador próximos
        y_medio > y_indicador and  # Dedo médio acima do indicador
        all(landmarks[i][1] > y_indicador for i in [14, 18])  # Anelar e mínimo abaixo do indicador
    )

    if polegar_cima:
        return "👍 Legal"
    elif ok_gesto:
        return "👌 Ok"
    return "Gesto não identificado"

# Captura de vídeo
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]

            # Debugging visual: Desenhar coordenadas dos dedos
            for idx, lm in enumerate(landmarks):
                h, w, _ = frame.shape
                cx, cy = int(lm[0] * w), int(lm[1] * h)
                cv2.putText(frame, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

            # Reconhecer gesto
            gesto = reconhecer_gesto(landmarks)
            cv2.putText(frame, gesto, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar frame
    cv2.imshow("Reconhecimento de Gestos", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
hands.close()
cv2.destroyAllWindows()
