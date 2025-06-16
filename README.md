# 🖐️ Hand Gesture Volume Controller (MacOS)

Control your Mac's **volume using just your fingers** — no clicks, no buttons!
Built with OpenCV + MediaPipe + Python. Works with your iPhone camera via Continuity.

---

## 📽️ Demo

> 📹 Raise your hand.
> 👆 Bring your thumb and index finger close = volume down
> ✋ Spread them apart = volume up
> 🔊 Real-time volume control right from the air!

---

## 🛠️ Features

* 🖐️ Tracks your hand with MediaPipe
* 📏 Calculates distance between thumb and index finger
* 🔊 Maps finger distance to Mac volume (0–100%)
* 🪟 Live video feed with hand landmarks
* 🎚️ Visual volume bar on screen

---

## 🚀 Quick Start

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/hand-gesture-volume-control.git
cd hand-gesture-volume-control
```

### 2. Create & activate a virtual environment

```bash
conda create -n vision_001 python=3.9 -y
conda activate vision_001
```

### 3. Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 4. Run the project

```bash
python main.py
```

> 📱 Make sure your iPhone Continuity Camera is connected and authorized
> Press `q` to quit

---

## 💻 Requirements

* macOS
* iPhone (as webcam via Continuity Camera)
* Python 3.9+
* Conda or virtualenv
* Camera permission for terminal

---

## 📂 Files

| File        | Description        |
| ----------- | ------------------ |
| `main.py`   | Main Python script |
| `README.md` | This file          |

---

## 🧠 How It Works (Simple)

1. Uses OpenCV to capture camera frames.
2. MediaPipe detects your hand and gives coordinates.
3. Measures distance between your thumb & index finger.
4. Converts that distance into a volume percentage.
5. Sets system volume using `osascript` on macOS.

---

## 🙋‍♂️ Made By

**Manav Desai**
AI & CV Engineer 🚀

> *"Controlling real-world systems with code is magical — so I built one with just my hand."*

