"""Local interactive Gradio application for WaterVision AI ONNX inference."""

import html
import os

import gradio as gr

from onnx_inference import DEFAULT_MODEL, predict_scores

CLASS_INFO = {
    "0_low": ("Low turbidity", "<5 FNU", "#38bdf8"),
    "1_moderate": ("Moderate turbidity", "5 to <20 FNU", "#fbbf24"),
    "2_high": ("High turbidity", "≥20 FNU", "#fb7185"),
}

if not DEFAULT_MODEL.is_file():
    raise FileNotFoundError(f"Model file not found: {DEFAULT_MODEL}")


def _score_panel(scores):
    rows = []
    for key, (label, range_text, color) in CLASS_INFO.items():
        score = float(scores.get(key, 0.0))
        width = max(0.0, min(100.0, score * 100))
        rows.append(
            "<div class='score-row'>"
            f"<div class='score-heading'><span>{html.escape(label)}</span>"
            f"<span>{html.escape(range_text)} · {score:.1%}</span></div>"
            "<div class='score-track'><div class='score-fill' "
            f"style='width:{width:.2f}%;background:{color}'></div></div></div>"
        )
    return "<div class='score-panel'>" + "".join(rows) + "</div>"


def classify_image(image_path, reference_fnu):
    if not image_path:
        return "<div class='empty-state'>Upload or select an image to run classification.</div>", "", ""

    scores = predict_scores(image_path)
    top_key = max(scores, key=scores.get)
    label, range_text, _ = CLASS_INFO[top_key]
    confidence = float(scores[top_key])
    prediction = (
        "<div class='prediction-card'>"
        "<div class='eyebrow'>MODEL OUTPUT · EXPERIMENTAL CATEGORY</div>"
        f"<div class='prediction'>{html.escape(label)}</div>"
        f"<div class='prediction-meta'>{html.escape(range_text)} · score {confidence:.1%}</div>"
        "</div>"
        + _score_panel(scores)
    )

    comparison = "<div class='compare-card'><b>Reference comparison</b><br>Not supplied for this image.</div>"
    if reference_fnu not in (None, ""):
        try:
            fnu = float(reference_fnu)
            if fnu < 0:
                raise ValueError("negative value")
            expected_key = "0_low" if fnu < 5 else "1_moderate" if fnu < 20 else "2_high"
            expected_label = CLASS_INFO[expected_key][0]
            match = expected_key == top_key
            verdict = "Category agrees" if match else "Category mismatch"
            tone = "match" if match else "mismatch"
            comparison = (
                f"<div class='compare-card {tone}'><b>{verdict}</b><br>"
                f"Reference: {fnu:g} FNU ({html.escape(expected_label)})"
                f"<br>Model: {html.escape(label)} ({confidence:.1%})</div>"
            )
        except (TypeError, ValueError):
            comparison = "<div class='compare-card mismatch'><b>Invalid reference</b><br>Enter a non-negative FNU value.</div>"

    note = (
        "Scores are model outputs, not calibrated probabilities or FNU measurements. "
        "This image classifier does not assess potability, pathogens, chemical contamination, "
        "or field safety."
    )
    return prediction, comparison, note


def clear_demo():
    return (
        "",
        None,
        "<div class='empty-state'>Upload or select an image to run classification.</div>",
        "<div class='compare-card'>Add a reference FNU value to compare categories.</div>",
        "Scores are not calibrated FNU measurements or drinking-water safety assessments.",
    )


CSS = """
:root { --block-background-fill: #0b1220; --body-background-fill: #070d18; --neutral-50: #111c2e; }
.gradio-container { max-width: 1120px !important; background: #070d18 !important; color: #e5edf8 !important; }
.hero { padding: 24px 4px 8px; }
.hero h1 { font-size: 2rem; margin: 0 0 6px; color: #f5f8ff; }
.hero p { color: #9fb0c8; margin: 0; }
.score-panel { display: grid; gap: 14px; padding: 18px; border: 1px solid #24334a; border-radius: 14px; background: #0e192a; }
.score-heading { display: flex; justify-content: space-between; gap: 12px; color: #dce7f6; font-size: .92rem; }
.score-heading span:last-child { color: #9fb0c8; font-variant-numeric: tabular-nums; }
.score-track { height: 10px; background: #1c2a3d; border-radius: 8px; overflow: hidden; margin-top: 8px; }
.score-fill { height: 100%; border-radius: 8px; transition: width .5s ease; }
.prediction-card,.compare-card,.empty-state { padding: 20px; border-radius: 14px; border: 1px solid #24334a; background: #0e192a; }
.prediction-card { border-left: 4px solid #38bdf8; }
.eyebrow { color: #91a5c1; font-size: .72rem; letter-spacing: .13em; font-weight: 700; }
.prediction { font-size: 1.55rem; font-weight: 700; margin-top: 8px; color: #f5f8ff; }
.prediction-meta { color: #a9bad0; margin-top: 4px; }
.compare-card { line-height: 1.7; }
.compare-card.match { border-left: 4px solid #34d399; }
.compare-card.mismatch { border-left: 4px solid #fb7185; }
.empty-state { color: #9fb0c8; min-height: 64px; }
footer { display: none !important; }
"""


with gr.Blocks(title="WaterVision AI · Local demo") as demo:
    gr.HTML(
        "<div class='hero'><h1>WaterVision AI</h1>"
        "<p>Interactive ONNX image classification · three experimental turbidity categories</p></div>"
    )
    with gr.Row(equal_height=False):
        with gr.Column(scale=5):
            image = gr.Image(
                value=os.environ.get("WATERVISION_DEMO_IMAGE") or None,
                type="filepath",
                label="Water image",
                height=390,
            )
            reference = gr.Textbox(
                value=os.environ.get("WATERVISION_REFERENCE_FNU", ""),
                label="Reference measurement (FNU, optional)",
                info="Used only to compare the model category with a known measurement.",
                placeholder="e.g. 32",
            )
            with gr.Row():
                run = gr.Button("Classify image", variant="primary")
                clear = gr.Button("Clear")
        with gr.Column(scale=6):
            output = gr.HTML(_score_panel({}))
            comparison = gr.HTML(
                "<div class='compare-card'>Add a reference FNU value to compare categories.</div>"
            )
            note = gr.Markdown(
                "Scores are not calibrated FNU measurements or drinking-water safety assessments."
            )

    run.click(classify_image, inputs=[image, reference], outputs=[output, comparison, note])
    image.change(classify_image, inputs=[image, reference], outputs=[output, comparison, note])
    reference.change(classify_image, inputs=[image, reference], outputs=[output, comparison, note])
    clear.click(clear_demo, inputs=[], outputs=[image, reference, output, comparison, note])


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=int(os.environ.get("WATERVISION_PORT", "7860")),
        share=False,
        theme=gr.themes.Base(),
        css=CSS,
    )
