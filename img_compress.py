from PIL import Image
import os


def reduce_image_size(input_path, output_path, target_size_kb=450):
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            print(f"Input file does not exist: {input_path}")
            return

        # Open the image
        img = Image.open(input_path)

        # Initial quality
        quality = 95

        # Save the image with the initial quality
        img.save(output_path, 'JPEG', quality=quality, optimize=True)

        # Adjust quality until file size is close to target
        while os.path.getsize(
                output_path) > target_size_kb * 1024 and quality > 10:
            quality -= 5
            img.save(output_path, 'JPEG', quality=quality, optimize=True)

        print(f"Final image size: {os.path.getsize(output_path) / 1024:.2f} KB")
        print(f"Final quality: {quality}")
    except PermissionError:
        print(f"Permission denied. Unable to access the file: {input_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
input_image = "/Users/sabbha/Desktop/hdfc_scanned.jpg"
output_image = "/Users/sabbha/Desktop/hdfc_scanned_compressed.jpg"

reduce_image_size(input_image, output_image, target_size_kb=450)