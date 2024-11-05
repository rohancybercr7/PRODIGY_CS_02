from PIL import Image
import numpy as np

# Function to load the image and convert it to a numpy array
def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    return np.array(img)

# Function to save the encrypted or decrypted image
def save_image(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

# Encryption function (simple XOR operation on pixel values)
def encrypt_image(image_array, key):
    encrypted_array = np.copy(image_array)
    rows, cols, _ = encrypted_array.shape
    
    for i in range(rows):
        for j in range(cols):
            # Perform XOR on each RGB channel with the key
            encrypted_array[i, j] = np.bitwise_xor(encrypted_array[i, j], key)
    
    return encrypted_array

# Decryption function (simple XOR operation on pixel values)
def decrypt_image(encrypted_array, key):
    decrypted_array = np.copy(encrypted_array)
    rows, cols, _ = decrypted_array.shape
    
    for i in range(rows):
        for j in range(cols):
            # Perform XOR to decrypt the image
            decrypted_array[i, j] = np.bitwise_xor(decrypted_array[i, j], key)
    
    return decrypted_array

# Generate a random key (a 3-tuple for RGB values, range 0-255)
def generate_key():
    return np.random.randint(0, 256, size=(3,), dtype=np.uint8)

# Function to encrypt and decrypt an image based on the user's choice
def main():
    image_path = input("Enter the path to the image: ")
    action = input("Do you want to encrypt or decrypt the image? (encrypt/decrypt): ").strip().lower()

    # Load the image
    image_array = load_image(image_path)

    if action == 'encrypt':
        key = generate_key()
        print(f"Using encryption key: {key}")
        encrypted_image = encrypt_image(image_array, key)
        save_image(encrypted_image, "encrypted_image.png")
        print("Image encrypted and saved as 'encrypted_image.png'.")
        
    elif action == 'decrypt':
        key_input = input("Enter the encryption key (as 'R,G,B' values): ")
        key = np.array([int(x) for x in key_input.split(',')], dtype=np.uint8)
        decrypted_image = decrypt_image(image_array, key)
        save_image(decrypted_image, "decrypted_image.png")
        print("Image decrypted and saved as 'decrypted_image.png'.")
    
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()



#decryption


#Enter the path to the image: encrypted_image.png
#Do you want to encrypt or decrypt the image? (encrypt/decrypt): decrypt
#Enter the encryption key (as 'R,G,B' values): 145,56,200
#Image decrypted and saved as 'decrypted_image.png'.

