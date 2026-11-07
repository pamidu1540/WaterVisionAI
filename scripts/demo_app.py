from pathlib import Path
import gradio as gr
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "watervision_yolo26n_full_v1_best.onnx"
CLASS_LABELS = {
    "0_low": "Low turbidity category (<5 FNU)",
    "1_moderate": "Moderate turbidity category (5 to <20 FNU)",
    "2_high": "High turbidity category (≥20 FNU)",
}

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = YOLO(str(MODEL_PATH))


def classify_image(image_path):
    if not image_path:
        return {}, "Upload an image to see the model's three category scores."
    result = model.predict(source=image_path, imgsz=320, verbose=False)[0]
    scores = result.probs.data.detach().cpu().tolist()
    probabilities = {
        CLASS_LABELS.get(result.names[index], str(result.names[index])): float(score)
        for index, score in enumerate(scores)
    }
    note = (
        "Experimental image classification only. These scores are not a calibrated "
        "FNU measurement or a drinking-water safety assessment."
    )
    return probabilities, note


demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="filepath", label="Choose a water image"),
    outputs=[
        gr.Label(num_top_classes=3, label="Model category scores"),
        gr.Markdown(label="Use limitation"),
    ],
    title="WaterVision AI — turbidity image demo",
    description=(
        "A YOLO26n-cls proof of concept trained to predict low, moderate, or high "
        "experimental turbidity categories from an image."
    ),
    article="The model runs on this computer. Do not use it to judge potability or water safety.",
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", share=False)
