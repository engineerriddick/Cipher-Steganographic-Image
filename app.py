"""
Project: Cipher Embedder - Steganographic Text Hider
Developer: EngineerRiddick
Contact: engineerriddick@gmail.com

Description:
This advanced Python script allows embedding a text message within an image file 
(JPG or PNG) using a simple steganographic technique. The text is seamlessly 
hidden within the image data, creating a ciphered image that visually remains 
identical to the original. The embedded message can be retrieved by reading 
the binary content of the file.

This project is designed for educational purposes and aims to provide developers 
with insights into foundational steganography and data hiding techniques. 
It is shared with the developer community under the MIT License to encourage 
collaboration and further innovation.

Example:
- Input Image: img_cat.jpg
- Cipher Text: "hello world"
- Output Image: steganographic_img_cat.jpg

How to Reveal the Hidden Text:
- **On Linux or macOS**: Open a terminal and use the `cat` command to display the 
  contents of the steganographic image. The hidden text will appear at the end:
  cat steganographic_img_cat.jpg

"""

import os

def Steganographic(image_path, cipher_text, output_path):
    """
    Hide a cipher text message within an image file using steganographic principles.

    Parameters:
    image_path (str): Path of the original image file (JPG or PNG).
    cipher_text (str): Text message to conceal within the image.
    output_path (str): Path to save the resulting steganographic image file.
    """
    # Check if the input image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Read the original image file as binary data
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Convert the cipher text to bytes
    cipher_bytes = cipher_text.encode('utf-8')

    # Combine the original image data and the cipher text bytes
    stego_data = image_data + b'\n' + cipher_bytes

    # Write the stego data to a new file
    with open(output_path, 'wb') as output_file:
        output_file.write(stego_data)

    print(f"Steganographic image created successfully! Saved at: {output_path}")


# Example usage
if __name__ == "__main__":
    # Specify the input image, cipher text, and output path
    image_path = "img_cat.jpg"
    cipher_text = "hello world"
    output_name = f"steganographic_{os.path.basename(image_path)}"
    output_path = os.path.join(os.path.dirname(image_path), output_name)

    try:
        Steganographic(image_path, cipher_text, output_path)
    except Exception as e:
        print(f"Error occurred: {e}")
