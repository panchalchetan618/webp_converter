from PIL import Image
import os


def convert_to_webp(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".avif")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(
                output_folder, os.path.splitext(filename)[0] + ".webp"
            )

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, "WEBP", quality=80)
                    print(f"Converted: {filename} → {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")


input_path = input("Where are images? ")
output_path = os.path.join(input_path, "converted_images")
convert_to_webp(input_path, output_path)
