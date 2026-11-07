# Model card: WaterVision AI YOLO26n-cls

## Artifact

The repository contains `models/watervision_yolo26n_full_v1_best.onnx`, an ONNX export supplied by the project owner. It corresponds by filename and notebook path to the Experiment 01 full-run checkpoint `models/yolo26n_full_v1/weights/best.pt`.

- Architecture/task: Ultralytics YOLO26n classification (YOLO26n-cls)
- Input used in training/export: 320 × 320 RGB images
- Classes: low (<5 FNU), moderate (5 to <20 FNU), high (≥20 FNU)
- Artifact size: 5.88 MiB
- SHA-256: `1f91883fd763ac87a25edb25489b66f4c3060eaa0dccf7a58bc78f5043b00aeb`
- Exported ONNX file metadata/runtime parity have not been independently validated in this workspace.

## Training provenance

Notebook training configuration for `yolo26n_full_v1`: pretrained `yolo26n-cls.pt` initialization; 50 epoch maximum; image size 320; batch 16; SGD with initial learning rate 0.005 and cosine schedule; weight decay 0.0005; patience 10; seed 42; deterministic mode enabled; AMP disabled; automatic augmentation disabled; random erasing 0.0. The notebook describes a site-separated train/validation/test split. These are notebook settings, not a verified record of the exact run execution or checkpoint provenance beyond the supplied filename.

## Intended use and exclusions

Educational and research demonstration of image-based three-category turbidity classification under the source project's study conditions. Not for drinking-water potability, pathogen or chemical assessment, regulatory compliance, public-health decisions, or field safety.

## Evaluation scope

The 55.29% accuracy, 49.62% balanced accuracy, and 0.4965 macro F1 are pooled out-of-fold metrics for three separate Experiment 02 fold models. They do not measure this Experiment 01 full-run ONNX artifact. No verified held-out metrics for this exact full-run ONNX file are available in this handoff.

## Risks and limitations

Performance may depend on camera, lighting, container, location, background, and experiment-family conditions. The model can underestimate high turbidity. Class probabilities are not calibrated FNU measurements. Use a calibrated turbidity meter and appropriate water testing for real decisions.

## License

The project follows AGPL-3.0 in light of Ultralytics' published licensing statement for trained models; the source dataset record declares AGPL-3.0-or-later. See [`../LICENSE`](../LICENSE) and [`licensing.md`](licensing.md). This card is not legal advice.
