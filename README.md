# WaterVision AI

**YOLO26n-cls proof of concept for three-class turbidity image classification.**

This repository documents a completed experimental study on 662 labeled Turbidivision images. The reported evaluation uses three-fold family-aware cross-validation. This is a research prototype; it does not measure drinking-water safety or replace a calibrated turbidity meter.

## Results

| Metric | Pooled out-of-fold result |
|---|---:|
| Accuracy | 55.29% (366/662) |
| Balanced accuracy | 49.62% |
| Macro F1 | 0.4965 |
| Majority-class accuracy baseline | 48.79% |

Per-fold held-out accuracy: fold 0 66.23% (n=231), fold 1 48.44% (n=192), fold 2 50.21% (n=239). Validation accuracy was substantially higher than held-out results in some runs; do not report validation scores as final performance. See [results and caveats](docs/results.md).

## Scope and labels

Three experimental FNU categories (low, moderate, high) were used. Exact category boundaries and source-to-label mapping must be confirmed against the original notebook/data manifest before reuse. FNU labels refer to the study's turbidity measurements, not potability.

## Repository contents

- `notebooks/watervision_colab.ipynb`: portable Colab workflow scaffold; configure Drive paths and dataset first.
- `scripts/train.py`: train one YOLO classification model on a prepared directory dataset.
- `scripts/predict.py`: run inference and print ranked class probabilities.
- `docs/methodology.md`: family-aware evaluation protocol and reproducibility notes.
- `docs/dataset.md`: provenance and license status.
- `docs/model_card.md`: intended use, limitations, and risk considerations.
- `results/summary.json`: reported aggregate and fold metrics.

## Quick start in Colab

1. Open the notebook and choose a GPU runtime.
2. Mount Drive and set `PROJECT_DIR` to your own project folder.
3. Verify you have permission to use the images and preserve the family-level split manifest.
4. Install `requirements.txt` and follow the notebook cells. The project does not include the dataset or trained weights.
5. For inference, supply the path to a specific checkpoint, such as the separately identified CV fold 2 checkpoint. Do not combine fold checkpoints or call one a unified model.

A compatible classification dataset directory should follow Ultralytics' `train/<class>`, `val/<class>`, and optionally `test/<class>` convention. This scaffold does not recreate the original family-aware splits; use the original manifest and split-generation code before claiming to reproduce the reported cross-validation.

## Model artifact status

The prior project record names a fold checkpoint at `models/experiment02/yolo26n_cv_fold2_v2/weights/best.pt` in the user's Drive. It was not present in the supplied workspace, and account-linked Drive access could not be used during this handoff. Consequently, no checkpoint download is attached here. Fold 2 is a single fold model, not a pooled ensemble or unified model.

## Dataset and license

The dataset is not included. Public release is blocked pending confirmation of the original dataset license, attribution requirements, and permission to redistribute images and labels. See [dataset notes](docs/dataset.md).

## Reproducibility and caveats

The reported scores are transcribed from the referenced conversation summary. Training hyperparameters, exact class boundaries, fold manifests, seeds, software versions, checkpoint hashes, and source license have not yet been independently verified from the Colab notebook or Drive artifacts. Treat this repository as a documentation and workflow scaffold until those are supplied. Do not use for field decisions, regulatory reporting, potability, health advice, or safety decisions.

## Citation

If you use this work, cite it as an experimental WaterVision AI project and cite the original Turbidivision dataset according to its verified license and citation guidance. Dataset citation details remain to be confirmed.
