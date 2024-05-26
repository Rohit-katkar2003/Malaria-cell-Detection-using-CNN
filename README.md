# Malaria-cell-Detection-using-CNN
In Malaria cell Detection i am going to use the Convolutional Neural Network along with the Web page on Streamlit
Overview
This project aims to classify malaria-infected cells from uninfected cells using Convolutional Neural Networks (CNN). Malaria is a life-threatening disease caused by parasites transmitted to people through the bites of infected female Anopheles mosquitoes. Early and accurate detection is crucial for effective treatment. This project leverages deep learning to automate the detection process, improving accuracy and efficiency.

Table of Contents
Overview
Dataset
Installation
Usage
Model Architecture
Training
Evaluation
Results
Contributing
License
Dataset
The dataset used for this project is the Cell Images for Malaria Detection. It consists of 27,558 images of blood smears, with equal instances of parasitized and uninfected cells.

Installation
To get started with the project, clone the repository and install the necessary dependencies:

bash
Copy code
git clone https://github.com/yourusername/malaria-cell-classification.git
cd malaria-cell-classification
pip install -r requirements.txt
Usage
To use the trained model for prediction, follow these steps:

Ensure you have the trained model file (model.h5).
Run the prediction script:
bash
Copy code
python predict.py --image-path path_to_image
Model Architecture
The Convolutional Neural Network (CNN) used in this project has the following architecture:

Input Layer: 3-channel RGB images of 130x130 pixels
Convolutional Layers: 3 layers with 32, 64, and 128 filters
Pooling Layers: MaxPooling after each convolutional layer
Fully Connected Layers: 2 layers with 128 and 64 units
Output Layer: Softmax layer with 2 units for binary classification
Training
To train the model, run the following command:

bash
Copy code
python train.py
This script will load the dataset, preprocess the images, and train the CNN model. The trained model will be saved as model.h5.

Evaluation
To evaluate the model on the test set, run:

bash
Copy code
python evaluate.py
This will load the trained model and provide metrics such as accuracy, precision, recall, and F1 score.

Results
The trained CNN model achieved the following performance metrics on the test set:

Accuracy: 96%
Precision: 95%
Recall: 97%
F1 Score: 96%
Contributing
We welcome contributions to enhance this project. To contribute, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to explore the code and improve the model. Your contributions are greatly appreciated! If you encounter any issues or have questions, please open an issue in the repository.
