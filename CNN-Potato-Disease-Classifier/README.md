# 🥔 Potato Disease Classification using a Convolutional Neural Network (CNN)

A deep learning project built with TensorFlow and Keras to accurately classify potato leaf images into three distinct categories: **Healthy**, **Early Blight**, and **Late Blight**. This tool is designed to help automate the detection of common diseases, potentially aiding in early intervention to protect crop yields.

---

### 📊 Key Results & Performance

- **Validation Accuracy:** Achieved **~92.66%** on the test dataset.
- **Model Performance:** The training history demonstrates a stable learning curve with minimal overfitting, confirmed by the validation accuracy and loss metrics.
- **Classification Report:** The model shows high precision and recall across all three classes, effectively distinguishing between healthy and diseased leaves.

![Training and Validation Accuracy/Loss Plot](https://github.com/user-attachments/assets/8f50ed83-02a5-4f2f-8b59-5d3051e00ec4)

---

### ⚙️ Tech Stack & Libraries

- **Frameworks:** TensorFlow, Keras
- **Libraries:** NumPy, Matplotlib, Scikit-learn
- **Dataset:** PlantVillage
- **Environment:** Jupyter Notebook / Google Colab

---

### 🧠 Model Architecture

The project utilizes a custom-built Convolutional Neural Network. The architecture was designed to effectively learn hierarchical features from the leaf images:

1.  **Input Layer:** Processes images of size (256, 256, 3).
2.  **Convolutional Layers:** Multiple `Conv2D` layers with `ReLU` activation functions to extract key features like edges, textures, and patterns on the leaves.
3.  **Pooling Layers:** `MaxPooling2D` layers to down-sample the feature maps, reducing computational complexity and preventing overfitting.
4.  **Flatten Layer:** Converts the 2D feature maps into a 1D vector.
5.  **Dense Layers:** Fully connected layers that perform the final classification.
6.  **Output Layer:** A `Dense` layer with a `softmax` activation function to output the probability for each of the three classes.

---

### 📋 Project Workflow

1.  **Data Loading & Preprocessing:** Loaded the image dataset from the PlantVillage repository. Images were resized and normalized.
2.  **Data Augmentation:** Applied transformations (e.g., rotation, flipping) to the training data to increase its diversity and make the model more robust to variations in real-world images.
3.  **Model Training:** Trained the CNN on the augmented dataset, using the Adam optimizer and Sparse Categorical Crossentropy as the loss function.
4.  **Evaluation:** Assessed the model's performance on a held-out test set to ensure its generalization capabilities.
5.  **Model Saving:** The trained model has been saved as an `.h5` file for easy reuse and future deployment.

---

### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AnasSayed27/AI-ML-Portfolio.git
    ```
2.  **Navigate into the project folder:**
    ```bash
    cd CNN-Potato-Disease-Classifier
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook Potato_Disease_Classifier.ipynb
    ```
    
---

### 🔮 Future Work

- **Deployment:** Deploy the trained model using a web framework like **FastAPI** to create a REST API for predictions.
- **Real-Time Application:** Integrate the API with a mobile application using **TensorFlow Lite** to allow for real-time disease detection in the field.

---

### 🙏 Credits & Acknowledgements

- This project was inspired by the **Codebasics Deep Learning Series**.
- The dataset is provided by the **PlantVillage** project.
