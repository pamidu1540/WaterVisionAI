# Local testing and demo capture

## Run one image from the command line

Install Python 3.10 or newer, then from the repository directory:

```bash
python -m venv .venv
```

Activate the environment (`.venv\\Scripts\\activate` on Windows, or `source .venv/bin/activate` on macOS/Linux), then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the exported full-run ONNX model against an image you have permission to use:

```bash
python scripts/predict.py --weights models/watervision_yolo26n_full_v1_best.onnx --source path/to/image.jpg --imgsz 320
```

The script prints scores for the three categories. The model reports categories, not a calibrated FNU reading. This ONNX file is the Experiment 01 full-run artifact; Experiment 02 pooled cross-validation metrics belong to three different fold models.

## Launch an upload-based local demo

```bash
python scripts/demo_app.py
```

Open the local address printed in the terminal (normally `http://127.0.0.1:7860`) and choose an image. The app binds to this computer only and does not create a public Gradio share link. Do not enable a public share link for private images.

## Capture a short LinkedIn demo

A simple 30–45 second recording can show:

1. The title, “WaterVision AI — experimental turbidity image classification.”
2. Uploading a water image you own or have permission to show.
3. The returned low/moderate/high category scores.
4. The limitation visible on screen: “Not a calibrated FNU measurement or potability/safety assessment.”
5. A closing frame with the public GitHub repository link and dataset/paper credits.

Suggested narration: “WaterVision AI is a YOLO26 image-classification proof of concept trained on Turbidivision images. It predicts one of three experimental turbidity categories from a photo. Our separate family-aware cross-validation experiment scored 55.29% pooled accuracy across 662 held-out predictions; that score is not a test metric for the full-run model shown here. The demo is educational and cannot determine whether water is safe to drink.”

Use your own image or an image whose reuse terms you have checked. Avoid showing personal account details, and do not imply that the demo verifies water safety. The model file is AGPL-3.0 under the project's stated Ultralytics licensing basis, and dataset attribution is in `docs/dataset.md`.
