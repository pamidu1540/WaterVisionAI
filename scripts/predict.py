from pathlib import Path
import argparse
from onnx_inference import DEFAULT_MODEL, predict_scores

p = argparse.ArgumentParser(description="Classify one image with the WaterVision ONNX model.")
p.add_argument("--weights", type=Path, default=DEFAULT_MODEL, help="Path to the WaterVision .onnx model")
p.add_argument("--source", type=Path, required=True, help="Path to an image file")
p.add_argument("--imgsz", type=int, default=320)
a = p.parse_args()
if not a.weights.is_file():
    p.error(f"Model file not found: {a.weights}")
if not a.source.is_file():
    p.error(f"Image file not found: {a.source}")
for class_name, score in sorted(predict_scores(a.source, a.weights, a.imgsz).items(), key=lambda item: item[1], reverse=True):
    print(f"{class_name}: {score:.4f}")
