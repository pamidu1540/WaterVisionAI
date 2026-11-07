from pathlib import Path
import argparse
from ultralytics import YOLO

p = argparse.ArgumentParser(description="Train YOLO26n-cls on prepared image folders.")
p.add_argument("--data", type=Path, required=True, help="Dataset root with train/<class> and val/<class> folders")
p.add_argument("--epochs", type=int, default=50)
p.add_argument("--imgsz", type=int, default=224)
p.add_argument("--batch", type=int, default=32)
p.add_argument("--device", default="0")
p.add_argument("--name", default="watervision_yolo26n_cls")
a = p.parse_args()
if not (a.data / "train").is_dir() or not (a.data / "val").is_dir():
    p.error("--data must contain train/ and val/ directories")
model = YOLO("yolo26n-cls.pt")
model.train(data=str(a.data), epochs=a.epochs, imgsz=a.imgsz, batch=a.batch, device=a.device, name=a.name)
