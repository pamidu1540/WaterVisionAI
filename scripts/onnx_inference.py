from pathlib import Path
import numpy as np
from PIL import Image, ImageOps
import onnxruntime as ort

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "models" / "watervision_yolo26n_full_v1_best.onnx"
CLASS_NAMES = ("0_low", "1_moderate", "2_high")
IMAGENET_MEAN = np.asarray((0.485, 0.456, 0.406), dtype=np.float32)
IMAGENET_STD = np.asarray((0.229, 0.224, 0.225), dtype=np.float32)
_SESSIONS = {}


def _session(model_path):
    path = str(Path(model_path).resolve())
    if path not in _SESSIONS:
        _SESSIONS[path] = ort.InferenceSession(path, providers=["CPUExecutionProvider"])
    return _SESSIONS[path]


def preprocess_image(image_path, imgsz=320):
    """Match Ultralytics classification inference: RGB, shortest-edge resize, center crop, ImageNet normalization."""
    image = ImageOps.exif_transpose(Image.open(image_path)).convert("RGB")
    width, height = image.size
    scale = imgsz / min(width, height)
    resized = image.resize(
        (round(width * scale), round(height * scale)),
        resample=Image.Resampling.BILINEAR,
    )
    left = round((resized.width - imgsz) / 2)
    top = round((resized.height - imgsz) / 2)
    image = resized.crop((left, top, left + imgsz, top + imgsz))
    array = np.asarray(image, dtype=np.float32) / 255.0
    array = (array - IMAGENET_MEAN) / IMAGENET_STD
    return np.transpose(array, (2, 0, 1))[None, ...].astype(np.float32)


def predict_scores(image_path, model_path=DEFAULT_MODEL, imgsz=320):
    session = _session(model_path)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    scores = np.asarray(session.run([output_name], {input_name: preprocess_image(image_path, imgsz)})[0])[0]
    if not (np.all(scores >= 0) and np.isclose(scores.sum(), 1.0, atol=1e-4)):
        exp = np.exp(scores - scores.max())
        scores = exp / exp.sum()
    return {CLASS_NAMES[index]: float(scores[index]) for index in range(len(CLASS_NAMES))}
