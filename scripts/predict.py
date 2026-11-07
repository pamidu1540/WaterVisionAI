from pathlib import Path
import argparse
from ultralytics import YOLO

p = argparse.ArgumentParser(description="Classify image(s) with a specified WaterVision checkpoint.")
p.add_argument("--weights", type=Path, required=True, help="Path to a specific .pt checkpoint")
p.add_argument("--source", required=True, help="Image file or directory")
p.add_argument("--imgsz", type=int, default=224)
a = p.parse_args()
if not a.weights.is_file():
    p.error(f"Checkpoint not found: {a.weights}")
model = YOLO(str(a.weights))
for result in model.predict(source=a.source, imgsz=a.imgsz, stream=True):
    probs = result.probs
    order = probs.data.argsort(descending=True).tolist()
    print(result.path)
    for idx in order:
        print(f"  {result.names[idx]}: {float(probs.data[idx]):.4f}")
