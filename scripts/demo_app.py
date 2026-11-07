import os
import gradio as gr
from onnx_inference import DEFAULT_MODEL, predict_scores

CLASS_LABELS = {
    "0_low": "Low turbidity category (<5 FNU)",
    "1_moderate": "Moderate turbidity category (5 to <20 FNU)",
    "2_high": "High turbidity category (≥20 FNU)",
}
if not DEFAULT_MODEL.is_file():
    raise FileNotFoundError(f"Model file not found: {DEFAULT_MODEL}")


def classify_image(image_path):
    if not image_path:
        return {}, "Select an image to display the category scores."
    scores = predict_scores(image_path)
    labeled = {CLASS_LABELS[name]: score for name, score in scores.items()}
    note = (
        "Experimental image classification. Scores are not calibrated FNU measurements "
        "or drinking-water safety assessments."
    )
    return labeled, note


demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(
        value=os.environ.get("WATERVISION_DEMO_IMAGE") or None,
        type="filepath",
        label="Water image",
    ),
    outputs=[
        gr.Label(num_top_classes=3, label="Category scores"),
        gr.Markdown(label="Interpretation"),
    ],
    title="WaterVision AI | Image classification demo",
    description="YOLO26n-cls model · 320 × 320 input · three experimental turbidity classes",
    article="Inference runs locally using ONNX Runtime.",
)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=int(os.environ.get("WATERVISION_PORT", "7860")),
        share=False,
    )
