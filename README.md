# 💚 Heart in Gestures

Heart in Gestures is a browser-based, gamified educational platform that teaches the **Ukrainian Sign Language (USL) alphabet** using **computer vision and AI-powered gesture recognition**.

Built by **team GrlPower** for the **Technovation Girls 2024–2025 global competition (Senior Division)**, the platform helps children, adults, and veterans with hearing impairments learn USL in an accessible and engaging way.

This project **adapts and extends** the open-source repository  
[**hand-gesture-recognition-using-mediapipe** by Kazuhito Takahashi](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe),  
customizing it for Ukrainian Sign Language, a browser-based learning game, and our own dataset.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
  - [Technovation Girls](#technovation-girls)
  - [Team](#team)
- [Architecture & Tech Stack](#architecture--tech-stack)

---

## 🧾 Project Overview

**Problem.** Children and adults with hearing impairments in Ukraine — including a growing number of veterans with war-related hearing loss — have very few **interactive, child-friendly tools** to learn Ukrainian Sign Language. Existing materials are often offline, outdated, or do not provide **real-time feedback** on signing accuracy.

**Solution.** Heart in Gestures is a **web-based game** where users:

- See a USL letter and example sign.
- Show the sign in front of their camera.
- Receive **instant feedback** from an AI model that recognizes the gesture.

### Technovation Girls

This project was created for **Technovation Girls**, a global technology entrepreneurship challenge where teams of girls (ages 13–18) build apps and AI solutions addressing problems in their communities.

Heart in Gestures (team **GrlPower**, Ukraine):

- Competes in the **Senior Division**.
- Uses **computer vision** to support **inclusive education** and **language equality**.
- Focuses on **Ukrainian Sign Language** learners, including children and veterans with hearing impairments.

### Team

**Team GrlPower (Participants):**

- Kyra Myronova
- Kateryna Chubko
- Anna Slysh
- Angelina Usenko  

**Mentor:**

- **Daria Goptsii** — Technical mentor & advisor on computer vision, and ML pipeline

---

## Architecture & Tech Stack

### High-level Architecture

1. **Front-end / UI**
   - Built with **Streamlit** (multi-page app under `pages/`).
   - Custom visual design via `style.css` and assets in `images/`.
   - Shows current target letter, reference sign image/animation, and game UI.

2. **Video & Hand Tracking**
   - **OpenCV** captures frames from the user’s webcam.
   - **MediaPipe Hands** detects 3D hand landmarks (21 keypoints per hand).

3. **Feature Extraction**
   - Landmarks are:
     - Converted to relative coordinates.
     - Normalized (scale-invariant).
     - Flattened into a **1D feature vector**.

4. **Gesture Classification (AI)**

   Lightweight TF Lite inference via `KeyPointClassifier`:

   ```python
   class KeyPointClassifier(object):
       def __init__(
           self,
           model_path='model/keypoint_classifier/keypoint_classifier.tflite',
           num_threads=1,
       ):
           self.interpreter = tf.lite.Interpreter(
               model_path=model_path,
               num_threads=num_threads
           )
           self.interpreter.allocate_tensors()
           self.input_details = self.interpreter.get_input_details()
           self.output_details = self.interpreter.get_output_details()

       def __call__(self, landmark_list):
           input_index = self.input_details[0]['index']
           self.interpreter.set_tensor(
               input_index,
               np.array([landmark_list], dtype=np.float32)
           )
           self.interpreter.invoke()
           output_index = self.output_details[0]['index']
           result = self.interpreter.get_tensor(output_index)
           result_index = np.argmax(np.squeeze(result))
           return result_index
