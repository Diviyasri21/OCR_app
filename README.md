# OCR_app 
**Hindi-English OCR Web Application**<br>
This is a web application that allows users to upload images and extract text in both Hindi and English using Optical Character Recognition (OCR) technology. The application leverages EasyOCR for text extraction and provides a user-friendly interface built with Streamlit.<br>

Table of Contents<br>

Features<br>
Requirements<br>
Setup Instructions<br>
Running the Application<br>
Deployment<br><br>

Features<br>

Upload images in JPEG or PNG format.<br>
Extract text from images in Hindi and English.<br>
Keyword search functionality to find specific terms in the extracted text.<br>
Adaptive image preprocessing to enhance OCR accuracy.<br><br>
Requirements<br>

To run this application, ensure you have the following installed:<br>

Python 3.7 or higher<br>
Streamlit<br>
EasyOCR<br>
OpenCV<br>
Pillow<br>
NumPy<br>
Setup Instructions<br>

Clone the Repository:<br> Clone this repository to your local machine using the following command:<br><br>
git clone https://github.com/Diviyasri21/OCR_app.git<br>
cd OCR_app<br>
Create a Virtual Environment (optional but recommended): <br>Create a virtual environment to manage dependencies:<br>

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`<br>
Install Required Packages:<br> Install the required packages using pip:<br>

pip install streamlit easyocr opencv-python pillow numpy<br><br>
Running the Application<br>

To run the web application locally, execute the following command:<br>

streamlit run app.py<br>  # Replace `app.py` with the name of your Python file if different<br><br>
This command will start the Streamlit server and open the application in your default web browser. You can then upload images and use the OCR functionality.<br><br>

Deployment<br>

To deploy the application, you can use platforms such as Heroku, Streamlit Sharing, or any cloud service that supports Python web applications. <br>Below are the steps for deploying on Streamlit Sharing:<br>

Push your code to a GitHub repository (if not already done).
Go to Streamlit Sharing and log in or sign up.
Click on 'New app' and select your GitHub repository.
Specify the main file (e.g., app.py).
Click 'Deploy' and wait for the deployment process to complete.
streamlit run /users/diviyaselladurai/documents/ocr_project/ocr_apph.py


For any inquiries or feedback, please contact:

Name: Diviyasri Selladurai
Email: diviyasris@karunya.edu.in <br>
This project demonstrates an easy way to extract text from images with both Hindi and English content, offering a powerful tool for multilingual OCR tasks.
