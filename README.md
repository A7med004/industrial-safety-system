# Industrial Safety System <POC>

A proof of concept that uses YOLOv8 to detect safety equipment (PPE) in video footage.

## Goal

Detect whether workers are wearing:

- Hardhats
- Safety vests

If a hardhat or vest is missing, the system highlights the detection in red and displays a **SAFETY VIOLATION** alert.

## Flow

```text
Video input → YOLOv8 detection → PPE check → Alerted output video
```

## Classes

- `Hardhat`
- `NO-Hardhat`
- `Safety Vest`
- `NO-Safety Vest`

## Run

Install dependencies:

```bash
pip install ultralytics opencv-python
```

Train the model:

```bash
python main.py
```

Run detection on `test.mp4`:

```bash
python video_test.py
```

The processed video is saved as `output.mp4`.

## Dataset

The project uses the [PPE Dataset for YOLOv8](https://www.kaggle.com/datasets/shlokraval/ppe-dataset-yolov8/data). Use `filter_dataset.py` to keep and remap the PPE classes used by the model.

## Notes

- Datasets, trained weights, and videos are excluded from the repository.
- This proof of concept does not include tracking or behavior analysis.
