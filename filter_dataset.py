import os
import shutil

ALLOWED_CLASSES = [3, 8, 13, 10]

MAPPING = {
    3: 0,   # Hardhat
    8: 1,   # NO-Hardhat
    13: 2,  # Safety Vest
    10: 3   # NO-Safety Vest
}

SPLITS = ["train", "valid", "test"]

BASE_INPUT = "dataset"
BASE_OUTPUT = "filtered"


def process_split(split):
    print(f"\n Processing {split}...")

    input_images = os.path.join(BASE_INPUT, split, "images")
    input_labels = os.path.join(BASE_INPUT, split, "labels")

    output_images = os.path.join(BASE_OUTPUT, split, "images")
    output_labels = os.path.join(BASE_OUTPUT, split, "labels")

    os.makedirs(output_images, exist_ok=True)
    os.makedirs(output_labels, exist_ok=True)

    total = 0
    kept = 0

    for file in os.listdir(input_labels):
        label_path = os.path.join(input_labels, file)

        with open(label_path, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            parts = line.strip().split()
            cls = int(parts[0])

            if cls in ALLOWED_CLASSES:
                parts[0] = str(MAPPING[cls])
                new_lines.append(" ".join(parts) + "\n")

        if new_lines:
            with open(os.path.join(output_labels, file), "w") as f:
                f.writelines(new_lines)

            img_name = file.replace(".txt", ".jpg")
            src_img = os.path.join(input_images, img_name)
            dst_img = os.path.join(output_images, img_name)

            if os.path.exists(src_img):
                shutil.copy(src_img, dst_img)
                kept += 1

        total += 1

    print(f" {split}: {kept}/{total} images kept")


def main():
    for split in SPLITS:
        process_split(split)

    print("\n Done! Filtered dataset is ready in /filtered")


if __name__ == "__main__":
    main()