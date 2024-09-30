import streamlit as st
from PIL import Image
import numpy as np
import cv2
import easyocr

# Preprocess the image to improve OCR accuracy
def preprocess_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding for better text recognition
    adaptive_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY, 11, 2)
    
    # Resize the image to improve OCR results
    resized_image = cv2.resize(adaptive_thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    
    return resized_image

# Extract text using EasyOCR
def extract_text_easyocr(image):
    reader = easyocr.Reader(['en', 'hi'])  # English and Hindi language support
    result = reader.readtext(np.array(image))
    
    # Combine all the detected text into a single string
    extracted_text = " ".join([text for (_, text, _) in result])
    
    return extracted_text

# Streamlit Web App
def main():
    st.title("Hindi-English OCR Web Application")
    st.write("Upload an image and extract text in both Hindi and English.")

    # File upload for image
    uploaded_file = st.file_uploader("Choose an image file (JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Open the image file
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Preprocess the image before OCR
        st.write("Processing...")
        preprocessed_image = preprocess_image(image)

        # Extract text using EasyOCR
        extracted_text = extract_text_easyocr(image)
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text_area("Extracted Text", extracted_text, height=200)

        # Keyword search in extracted text
        search_keyword = st.text_input("Enter keyword to search:")
        if search_keyword:
            if search_keyword in extracted_text:
                st.success(f"Keyword '{search_keyword}' found in the text.")
            else:
                st.warning(f"Keyword '{search_keyword}' not found in the text.")
    
    # Footer
    st.write("Powered by EasyOCR")

if __name__ == "__main__":
    main()
