# Cipher-Steganographic-Image
This project serves as an introductory tool for those interested in understanding steganography and data hiding techniques. Created by an experienced cryptography engineer, this script demonstrates the basic principle of embedding text messages within image files. It is designed to provide a clear and accessible foundation for students, researchers, and enthusiasts who wish to explore the fascinating world of steganography, a concept rooted in covert communication techniques dating back to the wartime era.

---

## 📌 Overview
The **Cipher-Steganographic-Image** script enables users to embed a text message into an image file (JPG or PNG) by appending the message at the binary level. The image remains visually identical to the original, but the embedded text can be retrieved using basic file reading methods. This script is ideal for:
- **Educational Purposes**: Learn the basics of steganography and its application in digital media.
- **Cryptography Enthusiasts**: Understand how covert communication techniques can be implemented programmatically.
- **Researchers**: Use as a starting point for exploring more advanced steganographic methods.

---

## ✨ Features
- **Seamless Message Embedding**: Appends text without altering the visual integrity of the image.
- **Support for JPG and PNG**: Compatible with widely used image formats.
- **Simple Concept**: Provides a basic approach for beginners to grasp the fundamentals of steganography.
- **Extendable**: Serves as an idea for more advanced implementations.

---

## 🗌 Requirements
- **Python 3.x**

---

## 🚀 Usage

Follow these steps to use the script:

1. **Prepare the Input**:
   - Place the input image file (e.g., `img_cat.jpg`) in the working directory.

2. **Specify the Message and Output**:
   - Define the text message to be hidden and the name of the output image.

3. **Run the Script**:
   - Execute the Python script to embed the message into the image.

### Example Usage
```python
image_path = "img_cat.jpg"
cipher_text = "hello world"
output_name = f"steganographic_{os.path.basename(image_path)}"
output_path = os.path.join(os.path.dirname(image_path), output_name)

Steganographic(image_path, cipher_text, output_path)
```

---

## 🖼️ Output

The resulting steganographic image will be saved as `steganographic_img_cat.jpg`. The image will appear identical to the original when viewed, but the hidden text can be revealed using simple tools.

---

## 🔍 How to Reveal the Hidden Text

### On Linux or macOS:
Use the `cat` command in the terminal to display the hidden text:
```bash
cat steganographic_img_cat.jpg
```

### On Windows:
Drag and drop the image file into Notepad or any text editor to view the hidden text.

---

## 🛠️ Basic Understanding of Steganography

Steganography is the art of hiding information within other media to conceal its existence. This concept has been used for covert communication since ancient times, especially during wartime, where spies and agents used techniques to hide messages in plain sight.

This project demonstrates a simple steganographic technique by appending a text message to the binary data of an image file. While basic, it provides a foundation for understanding how digital media can be leveraged for covert communication, inspiring further exploration into more sophisticated methods.

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided that appropriate credit is given to the original author. See the `LICENSE` file for more details.

---

## 📧 Contact

- **Developer**: EngineerRiddick  
- **Email**: engineerriddick@gmail.com

