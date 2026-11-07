# Local inference and demo

## Command-line inference

From the repository root, create a Python virtual environment and install the pinned minimum dependencies:

```bash
python -m venv .venv
```

Activate it (`.venv\\Scripts\\activate` on Windows or `source .venv/bin/activate` on macOS/Linux) and install requirements:

```bash
python -m pip install -r requirements.txt
```

Run inference on an image file:

```bash
python scripts/predict.py --weights models/watervision_yolo26n_full_v1_best.onnx --source path/to/image.jpg --imgsz 320
```

The output contains the model's scores for each category. The artifact predicts categories and does not return a calibrated FNU reading. Experiment 02 cross-validation scores describe separate fold models.

## Upload-based local interface

Launch the local interface with:

```bash
python scripts/demo_app.py
```

Open the loopback address printed by Gradio (default `http://127.0.0.1:7860`) and select an image. The application binds to `127.0.0.1` with Gradio sharing disabled; inference runs on the host machine. The output is an experimental category classification, not a potability or water-safety result.
