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

## Interactive local interface

```bash
python scripts/demo_app.py
```

Open `http://127.0.0.1:7860` in a browser and upload an image. The interface displays the image preview, three class scores, and the top predicted category. You can enter a reference FNU measurement to compare the reference category with the prediction, then clear the inputs and results to start again. The reference comparison is optional and is not a measurement produced by the model.

For a repeatable local demonstration, set `WATERVISION_DEMO_IMAGE` to an image path before starting the app; `WATERVISION_REFERENCE_FNU` optionally prefills a known reference value. `WATERVISION_PORT` selects a different local port. The application binds to `127.0.0.1`, disables Gradio sharing, and runs inference on the host machine. Model scores are not calibrated probabilities or FNU measurements; the classifier does not assess potability or field safety.
