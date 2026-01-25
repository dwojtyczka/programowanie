import cv2

class PersonDetector:
    def __init__(self, model_path, config_path):
        self.net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

    def policz_osoby(self, sciezka_do_obrazu):
        obraz = cv2.imread(sciezka_do_obrazu)
        if obraz is None:
            return 0

        blob = cv2.dnn.blobFromImage(obraz, size=(300, 300), swapRB=True, crop=False)
        self.net.setInput(blob)
        wykrycia = self.net.forward()

        licznik = 0
        for i in range(wykrycia.shape[2]):
            pewnosc = wykrycia[0, 0, i, 2]
            klasa_id = int(wykrycia[0, 0, i, 1])

            if klasa_id == 1 and pewnosc > 0.3:
                licznik += 1

        print(f"Wykryto: {licznik}")
        return licznik