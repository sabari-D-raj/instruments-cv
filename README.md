# Instrument CV - Hand Gesture Music Player

A real-time hand gesture recognition application that lets you play musical instruments by pointing your fingers at on-screen boxes. Stop all sounds by putting your hands down.

## 🎯 Project Goal

Create an interactive music experience where users can:
- **Play instruments** by pointing their index finger at colored boxes on the screen
- **Control sound playback** with hand gestures - pointing to play, hands down to stop
- **Multiple instruments** available: Drums, Guitar, Piano, and Trumpet
- Real-time hand detection and gesture recognition via webcam

## ✨ Features

- **Real-time Hand Detection** - Uses advanced computer vision to detect hand landmarks
- **Gesture Recognition** - Detects pointing gesture (index finger up, other fingers down)
- **Multi-instrument Support** - Play 4 different instruments:
  - 🥁 Drums (Green box)
  - 🎸 Guitar (Blue box)
  - 🎹 Piano (Red box)
  - 🎺 Trumpet (Yellow box)
- **Intuitive UI** - Color-coded boxes for easy instrument selection
- **Sound Control** - Audio automatically stops when hands are down
- **Low latency** - Smooth real-time performance

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Hand Detection** | MediaPipe | Real-time hand landmark detection and tracking |
| **Computer Vision** | OpenCV (cv2) | Video capture, frame processing, and UI rendering |
| **Audio** | Pygame (mixer) | Sound file loading and playback |
| **Language** | Python 3.x | Core application logic |

### Essential Dependencies

- `opencv-python` - Video capture and image processing
- `mediapipe` - Hand gesture recognition
- `pygame` - Audio playback and mixing
- Python 3.7+

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam/Camera
- Audio files in `music/` directory (drums.mp3, guitar.mp3, piano.mp3, trumpet.mp3)

### Setup

1. **Clone or download the repository:**
   ```bash
   cd path/to/insturmentCV
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe pygame
   ```

4. **Ensure audio files are present:**
   ```
   music/
   ├── drums.mp3
   ├── guitar.mp3
   ├── piano.mp3
   └── trumpet.mp3
   ```

## 🚀 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **How to play:**
   - Position yourself in front of the webcam
   - Point your index finger at one of the colored boxes to play that instrument
   - Keep other fingers down (curled)
   - Put your hand down to stop all sounds
   - Press 'Q' to quit the application

3. **Instrument Mapping:**
   - **Green Box (Left)** → Drums
   - **Blue Box** → Guitar
   - **Red Box** → Piano
   - **Yellow Box (Right)** → Trumpet

## 📁 Project Structure

```
insturmentCV/
├── main.py                 # Main application script
├── README.md              # This file
├── LICENSE                # License information
└── music/
    ├── drums.mp3
    ├── guitar.mp3
    ├── piano.mp3
    └── trumpet.mp3
```

## 🎮 How It Works

1. **Webcam Capture** - Continuously captures video frames from your webcam
2. **Hand Detection** - MediaPipe detects hand landmarks (27 points per hand)
3. **Gesture Recognition** - Checks if index finger is pointing:
   - Index finger tip is higher than middle knuckle (pointing up)
   - Middle, ring, and pinky fingers are down
4. **Position Detection** - Determines which instrument box the pointing finger is in
5. **Audio Playback** - Plays the corresponding instrument sound
6. **Sound Control** - Stops all audio when hands are down

## 🔧 Configuration

You can adjust the detection parameters in `main.py`:

- `min_detection_confidence=0.7` - Minimum confidence for hand detection
- `min_tracking_confidence=0.7` - Minimum confidence for hand tracking
- `cooldown=0.4` - Minimum time between sound triggers (in seconds)

## 📋 Requirements

- **Lighting**: Good lighting conditions for accurate hand detection
- **Distance**: Stand approximately 1-2 meters from camera
- **Space**: Clear background works best for detection accuracy
- **Permissions**: Camera access is required

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Hand not detected | Improve lighting, move closer to camera, adjust detection confidence |
| Audio not playing | Verify audio files exist in `music/` folder, check speaker volume |
| Jittery detection | Ensure good lighting and stable camera position |
| Application crashes | Ensure all dependencies are installed: `pip install -r requirements.txt` |

## 📝 License

See LICENSE file for details.

## 👨‍💻 Developer Notes

- The application uses a webcam at 0 (default camera)
- Display window is resized to 1200x800 for better visibility
- The pointing detection requires precise finger positioning
- Audio plays immediately upon detection with a cooldown period

---

**Enjoy making music with your hands! 🎵**