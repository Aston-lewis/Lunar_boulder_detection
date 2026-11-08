# 🌕 Lunar Boulder Detection

A computer vision project focused on detecting lunar craters and boulders using YOLO. The project aims to identify potential surface hazards and support lunar landing site analysis.

## 🚀 Features

- Detection of lunar craters and rocks using YOLO.
- Bounding-box visualization of detected objects.
- Support for lunar surface image analysis.
- Foundation for developing a lunar landing hazard mapping system.

## 🛠️ Tech Stack

- Python
- Ultralytics YOLO
- PyTorch
- OpenCV
- NumPy
- Matplotlib

## 📂 Project Structure

```text
Lunar_boulder_detection/
├── dataset/
├── runs/
├── .gitignore
├── labeled_sample.jpg
├── visualize_labels.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aston-lewis/Lunar_boulder_detection.git
cd Lunar_boulder_detection
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🛰️ Project Objective

The long-term objective is to develop a Lunar Boulder Hazard Mapper capable of identifying surface obstacles, estimating their dimensions and locations, and classifying terrain into safe, caution, and unsafe regions for potential lunar landing operations.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.