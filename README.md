# Audio-deepfake-detection

Foundation models have become powerful tools for generating text, images, and audio, often outperforming traditional methods. However, their ability to create highly convincing outputs poses significant security risks, particularly in the realm of AI-generated deepfake audio. These advanced techniques can easily bypass existing classifiers designed to distinguish legitimate, human-generated input from malicious manipulations. In this project, we focus on developing efficient and robust methods to detect AI-generated deepfake audio. By analyzing advanced attack strategies and leveraging state-of-the-art machine learning techniques, our goal is to enhance the security and reliability of audio-based systems against deepfake threats.


## Datasets

Dataset Information

The dataset used in this project was sourced from York University’s collection of audio datasets:

- [Main Dataset Page](https://bil.eecs.yorku.ca/datasets/)
- [Direct Download: for-rerec.tar.gz](https://www.eecs.yorku.ca/~bil/Datasets/for-rerec.tar.gz)

Dataset Description:

The dataset contains audio samples, both authentic and synthesized, to support research in deepfake audio detection. It is structured to facilitate training and testing of machine learning models.

## Preprocessing

The audio files in the dataset were converted to spectrograms for enhanced model performance. Spectrograms provide a visual representation of the spectrum of frequencies in the audio signals, making them highly suitable for deep learning techniques.


## Model 

1. Custom_CNN

Purpose:

This notebook demonstrates the creation of a custom Convolutional Neural Network (CNN) architecture for image classification tasks. It provides an end-to-end implementation, including data preprocessing, model definition, training, and evaluation.

Features:

Custom Architecture:

The network is built from scratch using layers such as convolutional, pooling, and dense layers. Adjustable hyperparameters like the number of filters, kernel size, and activation functions.

Data Handling:

Image data preprocessing, including resizing, normalization, and augmentation.

Training and Evaluation:

Loss and accuracy metrics visualization during training.

Model evaluation on test data.

Use Case:

Ideal for those looking to understand how to construct and fine-tune CNNs from the ground up for specific tasks.

2. VGG16.ipynb

Purpose:

This notebook leverages the pre-trained VGG16 model, a widely-used deep CNN architecture, for image classification. It demonstrates transfer learning techniques to adapt the model for custom datasets.

Features:

Transfer Learning:

Utilizes the pre-trained VGG16 model from TensorFlow/Keras. Includes options to freeze specific layers to retain pre-trained weights.

Fine-Tuning:

Modifies the top layers of the VGG16 model to suit the specific dataset.

Data Augmentation:

Implements advanced data augmentation techniques to enhance model generalization.

Performance Evaluation:

Includes confusion matrix and classification report to analyze model accuracy.

Use Case:

Best suited for scenarios where a robust, pre-trained architecture is needed for faster implementation and higher accuracy on smaller datasets.


## Model results


## Conclusion
