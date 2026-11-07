"""Export a WaterVision YOLO26n-cls checkpoint from Google Drive in Colab.

Run this file in a Colab cell after mounting Drive. Select the checkpoint
explicitly with MODEL_KIND before running. The script copies the checkpoint
into a named Drive exports folder, prints its SHA-256, and starts a browser
 download to the local computer.
"""
from pathlib import Path
import hashlib
import shutil

from google.colab import drive, files

# Choose exactly one: "full" or "cv-fold2".
# "full" is Experiment 01. "cv-fold2" is one fold-specific Experiment 02 model.
MODEL_KIND = "full"

DRIVE_ROOT = Path("/content/drive/MyDrive/WaterVisionAI")
SOURCES = {
    "full": DRIVE_ROOT / "models/yolo26n_full_v1/weights/best.pt",
    "cv-fold2": DRIVE_ROOT / "models/experiment02/yolo26n_cv_fold2_v2/weights/best.pt",
}
FILENAMES = {
    "full": "watervision_yolo26n_full_v1_best.pt",
    "cv-fold2": "watervision_yolo26n_cv_fold2_v2_best.pt",
}

if MODEL_KIND not in SOURCES:
    raise ValueError(f"MODEL_KIND must be one of {tuple(SOURCES)}")

drive.mount("/content/drive", force_remount=False)
source = SOURCES[MODEL_KIND]
if not source.is_file():
    raise FileNotFoundError(
        f"Checkpoint not found: {source}\n"
        "Check that Drive is mounted and this training run's best.pt exists."
    )

export_dir = DRIVE_ROOT / "exports"
export_dir.mkdir(parents=True, exist_ok=True)
destination = export_dir / FILENAMES[MODEL_KIND]
shutil.copy2(source, destination)

sha256 = hashlib.sha256()
with destination.open("rb") as stream:
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        sha256.update(chunk)

print(f"Model: {MODEL_KIND}")
print(f"Copied from: {source}")
print(f"Saved in Drive: {destination}")
print(f"Size: {destination.stat().st_size / (1024**2):.2f} MiB")
print(f"SHA-256: {sha256.hexdigest()}")
print("Starting download to this computer...")
files.download(str(destination))
