<div align="center">

# 🌍 Disaster Mitigation and Alert System  

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object--Detection-orange?style=for-the-badge&logo=yolo)
![Roboflow](https://img.shields.io/badge/Roboflow-Data-blueviolet?style=for-the-badge&logo=roboflow)
![WhatsAppKit](https://img.shields.io/badge/WhatsAppKit-green?style=for-the-badge&logo=whatsapp)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-red?style=for-the-badge&logo=opencv)
![HTML](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange?style=for-the-badge&logo=html5)

</div>

---

## 🧩 Introduction  

The **Disaster Mitigation and Alert System** is an AI-powered real-time detection and alert system that identifies potential disasters such as **fire, smoke, or flood** using camera input.  
It leverages the **YOLOv8 model** for high-speed object detection and automatically sends **WhatsApp alert messages** to all registered contacts via the **WhatsAppKit Python library** whenever a disaster is detected.  

This project aims to improve **emergency response times** and **minimize human loss** through instant alerts and automation.

---

## 📊 Data Details  

- **Source:** Self-annotated dataset created using **Roboflow**.  
- **Classes:** `Fire`, `Flood`, `Smoke`, `Earthquake_Aftermath`, etc.  
- **Type:** Object detection dataset (bounding box labels).  
- **Format:** YOLO format (`.jpg` + `.txt`)  
- **Dataset Split:**  
  - Train: 70%  
  - Validation: 20%  
  - Test: 10%  
- **Annotation Tool:** Roboflow Labeling Tool  
- **Augmentations:**  
  - Rotation, brightness variation, flipping, zoom  
  - Auto-resize to 640×640 for YOLO compatibility  

---

## 🧠 Model Details  

- **Model Used:** YOLOv8n (or YOLOv8s depending on deployment speed)  
- **Framework:** Ultralytics YOLO (PyTorch backend)  
- **Training Source:** Roboflow → Exported YOLOv8 dataset  
- **Input Size:** `640 × 640`  
- **Output:** Bounding boxes + confidence scores for disaster classes  
- **Loss Function:** Composite YOLO loss (Box + Class + Obj)  
- **Optimizer:** AdamW  
- **Epochs:** 50  
- **Validation Accuracy:** ~91% mAP@0.5  
- **Inference Speed:** ~20–25 FPS on mid-tier GPU  

### 🔍 Inference Flow:
```text
Frame Capture → Preprocessing → YOLOv8 Inference → Class Prediction → Confidence Check → Trigger Alert (if above threshold)
