from pathlib import Path
import cv2

stem = "-0_28360998131250864-1_0882708585247933-3_287897108937001-1_916016269099713_png.rf.42b43a9e416ae83cd0e2a30ab0f0ba79"

image_path = Path("dataset/train/images") / f"{stem}.jpg"
label_path = Path("dataset/train/labels") / f"{stem}.txt"

image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

height, width = image.shape[:2]

with open(label_path) as file:
    for line in file:
        values = list(map(float, line.split()))
        class_id, xc, yc, bw, bh = values

        x1 = int((xc - bw / 2) * width)
        y1 = int((yc - bh / 2) * height)
        x2 = int((xc + bw / 2) * width)
        y2 = int((yc + bh / 2) * height)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imwrite("labeled_sample.jpg", image)
print("Saved labeled_sample.jpg")
