# 🥔 Potato Disease Classifier - A Deep Learning Web App

This project is an end-to-end web application that uses a **Convolutional Neural Network (CNN)** to classify potato leaf images as **Healthy**, **Early Blight**, or **Late Blight**. Users can upload an image and receive a real-time prediction with a confidence score.

---

### ✨ Live Demo

This application is fully functional. Here is a demonstration of the user workflow:

![Potato Disease Classifier Demo GIF](https://github.com/AnasSayed27/AI-ML-Portfolio/blob/main/media/CNN-GIF.gif)

---

### 📊 Model Performance

- **Validation Accuracy:** **~92.66%** on the test dataset.
- The model demonstrates a stable learning curve with high precision and recall across all three classes.

---

### ⚙️ Tech Stack & Architecture

- **Backend:** FastAPI, Python
- **Frontend:** HTML, CSS (via a templates folder)
- **Deep Learning:** TensorFlow, Keras
- **Libraries:** NumPy, Scikit-learn, Pillow

---

### 🚀 How to Run Locally

1.  **Clone the Repository & Navigate to the Project:**
    ```bash
    git clone https://github.com/AnasSayed27/AI-ML-Portfolio.git
    cd Potato-Disease-Classification
    ```
2.  **Download the Model File:**
    Download the trained model (`model.h5`) from the [Google Drive link provided here](https://drive.google.com/file/d/1Y4tTJ00aDStkFY_ilKKsl9u4na6ZeuX0/view?usp=sharing) and place it in the root of this project folder. *(Note: This step requires Git LFS to be installed if cloning directly).*
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the FastAPI Server:**
    ```bash
    uvicorn app:app --reload
    ```
5.  **Access the App:** Open your web browser and go to `http://127.0.0.1:8000`.

---

### 📋 Project Workflow & Development

This project was developed in three key phases, moving from pure research to a functional application:

1.  **Experimentation & Training:** A Convolutional Neural Network (CNN) was designed and trained in a Jupyter Notebook. The focus was on achieving high accuracy and robust generalization using the PlantVillage dataset and data augmentation techniques.

2.  **AI-Assisted Application Scaffolding:** To accelerate the transition from research to a usable product, AI-assisted development was leveraged to rapidly scaffold the backend API and frontend interface. This involved generating the boilerplate code for the FastAPI routes and the basic HTML/CSS structure.

3.  **Core Logic & Integration:** With the application shell in place, the primary focus shifted to the core engineering challenge: seamlessly integrating the saved TensorFlow model (`.h5`) into the FastAPI backend. This included writing the logic for image preprocessing, making predictions, and ensuring the final output was correctly formatted and sent to the frontend.
---
