# WaterVision AI

**YOLO26n-cls proof of concept for three-category turbidity image classification.** This project fine-tunes a pretrained Ultralytics YOLO26n classification model on a 662-image labeled subset of the Turbidivision dataset.

## Model download

The user-provided ONNX export for the **Experiment 01 full run** is included at [`models/watervision_yolo26n_full_v1_best.onnx`](models/watervision_yolo26n_full_v1_best.onnx) (5.88 MiB). The GitHub repository is private, so users need access to download it. The checkpoint is distinct from the three Experiment 02 CV fold checkpoints; it is not a pooled CV model.

- Model: YOLO26n-cls fine-tuned checkpoint `yolo26n_full_v1`, exported to ONNX
- Training input size: 320 × 320
- Classes: `0_low` (<5 FNU), `1_moderate` (5 to <20 FNU), `2_high` (≥20 FNU)
- SHA-256: `1f91883fd763ac87a25edb25489b66f4c3060eaa0dccf7a58bc78f5043b00aeb`
- For a fresh export from Drive, see [`scripts/export_colab.py`](scripts/export_colab.py).

This full-run ONNX file does **not** inherit the pooled Experiment 02 CV results below. Those results summarize three different fold-specific models.

## Experiment 02 cross-validation results

| Metric | Pooled out-of-fold result |
|---|---:|
| Accuracy | 55.29% (366/662) |
| Balanced accuracy | 49.62% |
| Macro F1 | 0.4965 |
| Majority-class accuracy baseline | 48.79% |

Held-out accuracy by CV fold: fold 0 66.23% (n=231), fold 1 48.44% (n=192), fold 2 50.21% (n=239). These are three family-aware validation models and do not describe the Experiment 01 full-run ONNX artifact. See [results and caveats](docs/results.md).

## Dataset credit and license

The notebook downloads the Turbidivision v1.0.0 release and selects 662 images with usable FNU labels. The dataset record declares **AGPL-3.0-or-later**. We credit Ian M. Rudy and Matthew J. Wilson and link to the dataset DOI. The data are not included in this repository. Full attribution and license notes are in [`docs/dataset.md`](docs/dataset.md).

The related peer-reviewed paper is separately licensed CC BY 4.0; that article license does not replace or change the dataset record's license. See [Rudy & Wilson (2024)](https://doi.org/10.7717/peerj.18254).

## Code and model licensing

This repository is licensed under **GNU AGPL v3.0**. The project uses Ultralytics YOLO code and a YOLO26n classification model. Ultralytics states that its trained models fall under AGPL-3.0 by default, and that using its code/models requires AGPL-3.0 for the derivative project or an Ultralytics Enterprise license. This repository does not claim an Enterprise license. See [`LICENSE`](LICENSE), [Ultralytics license terms](https://www.ultralytics.com/license), and [`docs/licensing.md`](docs/licensing.md). The ONNX export remains subject to applicable upstream and dataset license terms; exporting to ONNX does not itself remove those terms.

## Repository contents

- `notebooks/watervision_colab.ipynb`: documented Colab workflow scaffold; it is not a byte-for-byte copy of the user's original notebook.
- `scripts/train.py`, `scripts/predict.py`, `scripts/export_colab.py`: training, inference, and Drive export helpers.
- `docs/methodology.md`: family-aware evaluation protocol and reproducibility notes.
- `docs/dataset.md`, `docs/licensing.md`: attribution and license separation.
- `docs/model_card.md`: intended use and limitations.
- `docs/results.md`, `results/summary.json`: reported CV results and scope cautions.

## Safety and limitations

This model predicts experimental image categories only. It does not evaluate potability, pathogens, chemical contamination, regulatory compliance, or field safety. It must not guide drinking-water decisions. A calibrated turbidity meter and appropriate water-quality tests are required for real measurements and safety decisions.
