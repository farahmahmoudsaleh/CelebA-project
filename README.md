# 🧠 CelebA Facial Attribute Classification with ResNet

This project implements a deep learning pipeline for **multi-label classification** of facial attributes using the **CelebA dataset** and a **ResNet-based CNN model**. The project is structured using the **MVC (Model-View-Controller)** pattern for clean separation of concerns and supports **Docker** for seamless deployment and testing.

---

## 📂 Project Structure (MVC Pattern)
```
celebA_cnn_project/
├── model/
│   ├── model_loader.py     # Load model from .pkl file
│   └── predictor.py        # Send image to the model and get predictions
├── view/
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── controller/
│   └── routes.py
├── utils/
│   └── image_utils.py      # Create transforms and load image
├── requirements.txt        # Dependencies
├── README.md
└── .gitignore

```

## 🧠 Model Overview

- ✅ Backbone: `ResNet18`
- ✅ Output Layer: 3 sigmoid neurons for attribute prediction
- ✅ Loss Function: `BCEWithLogitsLoss`
- ✅ Optimizer: `Adam`
- ✅ Augmentations: Resize, Normalize, RandomHorizontalFlip, Color Jitter.

---

## 🐳 Docker Support

You can run the full project in a Docker container:

```bash
docker pull farahmsaleh/celeba-classifier

docker run -p 8000:8000 farahmsaleh/celeba-classifier

open link : http://127.0.0.1:8080/
