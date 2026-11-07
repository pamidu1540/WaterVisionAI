# Local inference and demo

## Environment

The inference-only package list avoids the model-training framework and uses ONNX Runtime:

```bash
python -m venv .venv
```

Activate the environment (`.venv\\Scripts\\activate` on Windows or `source .venv/bin/activate` on macOS/Linux), then install:

```bash
python -m pip install -r requirements-inference.txt
```

## Command-line inference

```bash
python scripts/predict.py --weights models/watervision_yolo26n_full_v1_best.onnx --source path/to/image.jpg --imgsz 320
```

The command prints scores for low (<5 FNU), moderate (5 to <20 FNU), and high (≥20 FNU) categories. Preprocessing follows the Ultralytics classification inference pipeline: EXIF correction, RGB conversion, shortest-edge resize, center crop, and ImageNet normalization.

## Upload-based local interface

```bash
python scripts/demo_app.py
```

Open `http://127.0.0.1:7860` in a browser and select an image. The application binds to loopback with Gradio sharing disabled; inference runs on the host machine. The output is an experimental category classification, not a calibrated FNU reading.

For a repeatable local demonstration, set `WATERVISION_DEMO_IMAGE` to an image path before starting the app; the path is used to prefill the input. `WATERVISION_PORT` optionally selects a different local port. Neither setting enables external sharing.
