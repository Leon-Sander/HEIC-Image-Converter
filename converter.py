import os
from PIL import Image
from pillow_heif import register_heif_opener
import argparse

register_heif_opener()

def convert_heic_to_png_or_jpg(input_dir, output_dir, output_format='PNG'):
    """
    Convert HEIC images to PNG or JPG.
    
    :param input_dir: Directory containing HEIC images.
    :param output_dir: Directory to save converted images.
    :param output_format: Output format ('PNG' or 'JPEG').
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(input_dir, filename)
            try:
                with Image.open(heic_path) as img:
                    output_file = os.path.splitext(filename)[0] + ('.png' if output_format == 'PNG' else '.jpg')
                    output_path = os.path.join(output_dir, output_file)
                    img.save(output_path, output_format)
                    print(f"Converted {filename} to {output_file}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

def convert_single_heic(input_file, output_file, output_format='PNG'):
    """
    Convert a single HEIC image to PNG or JPG.
    
    :param input_file: Path to the HEIC file.
    :param output_file: Path to save the converted image.
    :param output_format: Output format ('PNG' or 'JPEG').
    """
    try:
        with Image.open(input_file) as img:
            img.save(output_file, output_format)
            print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert HEIC images to PNG or JPG.")
    parser.add_argument('--file', type=str, help="Path to a single HEIC file to convert.")
    parser.add_argument('--dir', type=str, help="Path to a directory containing HEIC images.")
    parser.add_argument('--output', type=str, required=True, help="Directory to save converted images.")
    parser.add_argument('--format', type=str, choices=['PNG', 'JPEG'], default='PNG', help="Output format ('PNG' or 'JPEG').")
    
    args = parser.parse_args()

    if args.file and args.dir:
        print("Please provide either a file or a directory, not both.")
        return
    
    if not args.file and not args.dir:
        print("Please provide either a file or a directory.")
        return

    if args.file:
        output_file = os.path.join(args.output, os.path.splitext(os.path.basename(args.file))[0] + ('.png' if args.format == 'PNG' else '.jpg'))
        convert_single_heic(args.file, output_file, args.format)
    
    if args.dir:
        convert_heic_to_png_or_jpg(args.dir, args.output, args.format)

if __name__ == "__main__":
    main()