# Results

## Experiment 02: family-aware cross-validation

| Evaluation | Images | Accuracy | Macro F1 |
|---|---:|---:|---:|
| Fold 0 held-out | 231 | 66.23% | 0.6159 |
| Fold 1 held-out | 192 | 48.44% | 0.3718 |
| Fold 2 held-out | 239 | 50.21% | 0.4565 |
| Pooled out-of-fold | 662 | 55.29% | 0.4965 |

Pooled balanced accuracy is 49.62%. Majority-class accuracy is 48.79%, and the project report records 366 correct predictions out of 662. The reported 91.11% validation accuracy for fold 2 is separate from its 50.21% held-out test accuracy.

These metrics correspond to `yolo26n_cv_fold0_v2`, `yolo26n_cv_fold1_v2`, and `yolo26n_cv_fold2_v2`. They do not evaluate the Experiment 01 full-run ONNX artifact.

## Experiment 01: full run

The notebook specifies `yolo26n_full_v1` and a site-separated train/validation/test split. The ONNX artifact in this repository is identified as the export of that run. A verified held-out metrics file for this artifact was not available.

Values in this document are transcribed from project outputs; the original prediction CSV files were not available here for recalculation.
