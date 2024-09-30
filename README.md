# OCR_app
**Hindi-English OCR Web Application
**
This project is a web-based Optical Character Recognition (OCR) application that extracts text from images containing both Hindi and English text. The application is built using Streamlit for the frontend, EasyOCR for text extraction, and OpenCV for image preprocessing. This project allows users to upload images and extract multilingual text from them.

**Features**

Multilingual OCR: Supports both Hindi and English text extraction using EasyOCR.
Image Preprocessing: Enhances image quality using OpenCV techniques such as grayscale conversion and adaptive thresholding to improve OCR accuracy.
User-friendly Interface: Built with Streamlit, allowing users to easily upload images and view extracted text.
Keyword Search: Users can input a keyword to search within the extracted text.

**Tech Stack**
Streamlit: Used for creating the web application interface.
EasyOCR: OCR engine that supports multiple languages, including Hindi and English.
OpenCV: Used for preprocessing the image to enhance the quality of text recognition.
Pillow: For handling image operations.
Setup Instructions

**Prerequisites**
Ensure that you have Python installed. 


Step 1: Install Required Packages
Install the necessary libraries using pip:


pip install streamlit opencv-python-headless easyocr pillow
Step 2: Run the Application
To start the OCR web application, run the following command in the terminal:


streamlit run ocr_app.py
Step 3: Using the Application
Upload an Image: Use the "Choose an image file" option to upload a file in .jpg, .jpeg, or .png format.
Text Extraction: Once the image is uploaded, the application will process the image and display the extracted text.
Keyword Search: Enter a keyword in the text input box to search for specific text in the extracted results.
Project Structure



The application applies the following image preprocessing techniques to enhance the accuracy of OCR:

Grayscale Conversion: Converts the image to grayscale to reduce noise and improve clarity.
Adaptive Thresholding: Applies adaptive thresholding to improve the visibility of text, especially for scanned documents or images with varying lighting conditions.
Resizing: Enlarges the image to help OCR engines better recognize small text.



Contributions

Contributions are welcome! Feel free to submit a Pull Request or open an issue if you find a bug or have suggestions for improvements.

Contact

For any inquiries or feedback, please contact:

Name: Diviyasri Selladurai
Email: diviyasris@karunya.edu.in
This project demonstrates an easy way to extract text from images with both Hindi and English content, offering a powerful tool for multilingual OCR tasks.
