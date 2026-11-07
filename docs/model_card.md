# Model card: WaterVision AI YOLO26n-cls

## Model identity

- Architecture and task: Ultralytics YOLO26n classification (YOLO26n-cls)
- Artifact: `models/watervision_yolo26n_full_v1_best.onnx`
- Run: Experiment 01, `yolo26n_full_v1`
- Input: 320 × 320 pixels
- Labels: low (<5 FNU), moderate (5 to <20 FNU), high (≥20 FNU)
- File size: 5.88 MiB
- SHA-256: `1f91883fd763ac87a25edb25489b66f4c3060eaa0dccf7a58bc78f5043b00aeb`

The ONNX file was supplied as the Experiment 01 export. Its runtime parity against the source PyTorch checkpoint was not independently evaluated as part of repository preparation.

## Training configuration

The notebook specifies pretrained `yolo26n-cls.pt` initialization, up to 50 epochs, batch size 16, image size 320, SGD, initial learning rate 0.005, cosine learning-rate schedule, weight decay 0.0005, patience 10, seed 42, deterministic mode, AMP disabled, automatic augmentation disabled, and random erasing 0.0. The notebook describes a site-separated train/validation/test split. The exact checkpoint execution record was not available for independent audit.

## Intended application

Research and educational evaluation of image-based classification into three experimental turbidity categories.

## Evaluation

The reported 55.29% accuracy, 49.62% balanced accuracy, and 0.4965 macro F1 are pooled out-of-fold results for the separate Experiment 02 fold models. They are not performance estimates for this Experiment 01 ONNX artifact. A verified held-out metric report for this exact artifact was not available.

## Limitations

The model predicts image categories rather than calibrated FNU measurements. Performance may vary with camera, illumination, container, location, background, and experiment family. The cross-validation fold accuracies ranged from 48.44% to 66.23%; the source report also indicates frequent confusion between moderate and high turbidity. No field validation or potability assessment is reported.

## License

The project follows AGPL-3.0 based on the identified Ultralytics terms for trained models. The dataset record declares AGPL-3.0-or-later. See [LICENSE](../LICENSE) and [licensing notes](licensing.md).
