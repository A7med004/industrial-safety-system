# Industrial Safety System

Computer-vision proof of concept for detecting personal protective equipment (PPE) on workers in video footage. The system uses a custom-trained YOLOv8 model to identify hardhats and safety vests, then highlights missing PPE as a safety violation.

## What it detects

| Class | Meaning |
| --- | --- |
| `Hardhat` | A worker is wearing a hardhat |
| `NO-Hardhat` | A worker is missing a hardhat |
| `Safety Vest` | A worker is wearing a safety vest |
| `NO-Safety Vest` | A worker is missing a safety vest |

When a missing-PPE class is detected, the output frame is marked in red and displays a **SAFETY VIOLATION** alert.

## How it works

```text
Video or camera input
        |
        v
Frame extraction
        |
        v
YOLOv8 PPE detection
        |
        v
Violation check (missing hardhat or vest)
        |
        v
Annotated video and on-screen alert
```

## Project structure

```text
.
|-- main.py              # Train a YOLOv8 model
|-- video_test.py        # Run detection on a video and save the result
|-- val.py               # Validate a trained model and print metrics
|-- filter_dataset.py    # Keep and remap PPE classes from the source dataset
|-- data.yaml            # YOLO dataset configuration
|-- dataset/             # Source dataset (not committed)
|-- filtered/            # Processed dataset (not committed)
|-- runs/                # Training outputs and model weights (not committed)
`-- weights/             # Optional local model weights (not committed)
```

## Requirements

- Python 3.10 or newer
- A webcam or video file for inference
- NVIDIA GPU and CUDA are recommended for training, but not required

Install the Python dependencies:

```bash
pip install ultralytics opencv-python
```

## Dataset preparation

This project uses the [PPE Dataset for YOLOv8](https://www.kaggle.com/datasets/shlokraval/ppe-dataset-yolov8/data).

1. Download and extract the dataset into `dataset/`.
2. Run the filtering script to retain and remap the four PPE classes:

   ```bash
   python filter_dataset.py
   ```

3. Confirm that `data.yaml` points to the resulting `filtered/train/images` and `filtered/valid/images` folders.

## Train

Train the model using the configured dataset:

```bash
python main.py
```

Training results and the best checkpoint are written under `runs/detect/`. Update the model path in `video_test.py` or `val.py` if your run directory has a different name.

## Run video detection

1. Put your input video at `test.mp4`, or change `video_path` in `video_test.py`.
2. Set the `best.pt` path in `video_test.py` to your trained checkpoint.
3. Run:

   ```bash
   python video_test.py
   ```

The application opens a preview window and writes the annotated result to `output.mp4`. Press <kbd>Esc</kbd> to stop early.

## Validate

Evaluate a trained model on the validation split:

```bash
python val.py
```

The script prints precision, recall, mAP@50, and mAP@50-95, with per-class metrics. Validation plots are saved in the YOLO run directory.

## Notes

- Large artifacts—datasets, checkpoints, videos, and training outputs—are intentionally excluded from version control. Share trained weights separately (for example, through a release or cloud storage) if they are needed by others.
- This is a detection proof of concept. It does not yet include person tracking, identity matching, or behavior analysis.

## License

No license has been selected yet. Add one before distributing or accepting external contributions.
