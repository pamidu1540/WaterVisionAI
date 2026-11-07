# Results

The source notebook and conversation reported two distinct sets of experiments.

## Experiment 02: three-fold family-aware cross-validation

| Evaluation | N | Accuracy | Macro F1 |
|---|---:|---:|---:|
| Fold 0 held-out | 231 | 66.23% | 0.6159 |
| Fold 1 held-out | 192 | 48.44% | 0.3718 |
| Fold 2 held-out | 239 | 50.21% | 0.4565 |
| Pooled out-of-fold | 662 | 55.29% | 0.4965 |

Pooled balanced accuracy: 49.62%. Majority-class baseline accuracy: 48.79%. Reported correct predictions: 366/662. Fold 2 validation accuracy of 91.11% is not its test accuracy.

These metrics refer to three fold-specific checkpoints (`yolo26n_cv_fold0_v2`, `fold1_v2`, `fold2_v2`), not the full-run model distributed as ONNX.

## Experiment 01 full run

The supplied notebook names a separate `yolo26n_full_v1` checkpoint trained with a site-separated split. The supplied ONNX artifact corresponds by name/path to that run, but this repository does not have a verified metrics file for that exact artifact. Do not attribute Experiment 02 pooled metrics to it.

The values above are transcribed from the project record, not independently recomputed from the prediction CSVs in this workspace. Original fold prediction files and evaluation code are needed to reproduce them independently.
