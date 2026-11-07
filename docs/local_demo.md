# Local image testing and demo

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

The script prints scores for the three categories. This model reports categories, not a calibrated FNU reading. It is the Experiment 01 full-run artifact; Experiment 02 pooled cross-validation metrics belong to three different fold models.

## Launch the local upload demo

```bash
python scripts/demo_app.py
```

Open the local address printed in the terminal (normally `http://127.0.0.1:7860`) and choose an image. The app binds to this computer only and does not create a public Gradio share link. Uploaded images are processed locally by the model. Do not use the app to make drinking-water safety decisions.
