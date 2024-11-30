
# HEIC to PNG/JPG Converter

A Python script to convert HEIC images to PNG or JPG formats. This script supports both single-file conversion and batch conversion from a directory.

## Features

- Convert a single HEIC image to PNG or JPG.
- Batch convert all HEIC images in a directory.
- Supports custom output directories.
- Easy-to-use with command-line arguments.

## Prerequisites

1. Python 3.6 or later
2. Install the required Python libraries:
   ```bash
   pip install pillow pillow-heif
   ```

   > **Note**: On Linux, ensure `libheif` is installed for proper HEIC decoding.

## Usage

### Convert a Single HEIC File
Convert a single HEIC file to PNG or JPG format:
```bash
python convert_heic.py --file /path/to/image.heic --output /path/to/output --format PNG
```

### Convert a Directory of HEIC Files
Batch convert all HEIC files in a directory:
```bash
python convert_heic.py --dir /path/to/input/directory --output /path/to/output --format JPEG
```

### Arguments

| Argument         | Description                                                  | Required |
|-------------------|--------------------------------------------------------------|----------|
| `--file`         | Path to a single HEIC file to convert.                        | Optional |
| `--dir`          | Path to a directory containing HEIC images.                  | Optional |
| `--output`       | Directory to save converted images.                          | Yes      |
| `--format`       | Output format: `PNG` or `JPEG` (default: `PNG`).             | No       |

> **Note**: Either `--file` or `--dir` must be provided, but not both.

## Example

### Single File Conversion
Convert a single HEIC image to a PNG:
```bash
python convert_heic.py --file /images/photo.heic --output /images/converted --format PNG
```

### Batch Conversion
Convert all HEIC images in a directory to JPG:
```bash
python convert_heic.py --dir /images/heic_photos --output /images/jpg_photos --format JPEG
```
