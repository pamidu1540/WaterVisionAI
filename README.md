# WaterVision AI

YOLO26n-cls proof of concept for three-category turbidity image classification. The project uses a 662-image labeled subset of the Turbidivision dataset and reports a separate three-fold family-aware cross-validation experiment.

## Model artifact

[Download the Experiment 01 full-run ONNX model](models/watervision_yolo26n_full_v1_best.onnx) (5.88 MiB).

| Property | Value |
|---|---|
| Architecture/task | Ultralytics YOLO26n-cls image classification |
| Run identity | `yolo26n_full_v1` (Experiment 01) |
| Input size | 320 × 320 pixels |
| Classes | low (<5 FNU), moderate (5 to <20 FNU), high (≥20 FNU) |
| SHA-256 | `1f91883fd763ac87a25edb25489b66f4c3060eaa0dccf7a58bc78f5043b00aeb` |

The artifact is a single full-run model. It is separate from the three fold-specific models used to compute Experiment 02 cross-validation metrics. The reported pooled scores below do not evaluate this ONNX file.

## Local inference

```bash
python -m pip install -r requirements-inference.txt
python scripts/predict.py --weights models/watervision_yolo26n_full_v1_best.onnx --source path/to/image.jpg --imgsz 320
```

The upload interface is available with `python scripts/demo_app.py`; setup details are in [Local inference and demo](docs/local_demo.md). For a Colab export from Drive, see [`scripts/export_colab.py`](scripts/export_colab.py).

## Experiment 02: family-aware cross-validation

| Metric | Pooled out-of-fold result |
|---|---:|
| Accuracy | 55.29% (366/662) |
| Balanced accuracy | 49.62% |
| Macro F1 | 0.4965 |
| Majority-class accuracy baseline | 48.79% |

Held-out accuracy was 66.23% (n=231), 48.44% (n=192), and 50.21% (n=239) for folds 0, 1, and 2 respectively. See [results](docs/results.md) and [methodology](docs/methodology.md). Metrics are transcribed from project outputs and have not been independently recalculated in this repository.

## Dataset attribution

Rudy, I. M., & Wilson, M. J. (2024). *Underwater Image/Turbidity Dataset* (1.0.0) [Data set]. Zenodo. [doi:10.5281/zenodo.10951021](https://doi.org/10.5281/zenodo.10951021). The dataset record declares AGPL-3.0-or-later. The raw dataset is not included. The related article, Rudy & Wilson (2024), *PeerJ* 12:e18254, is separately licensed CC BY 4.0. Attribution and provenance details are in [docs/dataset.md](docs/dataset.md).

## Licensing

The repository code and model are distributed under AGPL-3.0, following the Ultralytics licensing terms identified for YOLO code and trained models. The dataset record declares AGPL-3.0-or-later. The paper's CC BY 4.0 license applies to the article. See [LICENSE](LICENSE) and [licensing notes](docs/licensing.md). The project does not claim an Ultralytics Enterprise license.

## Technical documentation

- [Methodology](docs/methodology.md)
- [Results](docs/results.md)
- [Model card](docs/model_card.md)
- [Dataset provenance and attribution](docs/dataset.md)
- [Licensing notes](docs/licensing.md)
- [Local inference and demo](docs/local_demo.md)
- [Colab workflow notebook](notebooks/watervision_colab.ipynb)

## Scope

The classifier predicts one of three project-defined image categories. It is not a calibrated turbidity instrument and does not assess drinking-water potability, pathogens, chemical contamination, or regulatory compliance.
