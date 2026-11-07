# Experimental methodology

## Objective
Evaluate image classification for three project-defined turbidity categories, with generalization assessed across experiment families.

## Data and preprocessing
The supplied notebook retrieves Turbidivision release v1.0.0 and retains 662 images with usable FNU labels. Labels are mapped as low (<5 FNU), moderate (5 to <20 FNU), and high (≥20 FNU). Images are converted to RGB, EXIF orientation is applied, and each image is resized to fit within 1024 × 1024 pixels while preserving aspect ratio. Prepared images are encoded as JPEG at quality 92. Source and licensing details are recorded in [dataset.md](dataset.md).

## Experiment 01: site-separated full run
The notebook defines a site-separated train/validation/test split and trains `yolo26n_full_v1` from pretrained `yolo26n-cls.pt`. The corresponding ONNX export is included in `models/`. A verified test metric file for this artifact was not available when this repository was prepared.

Notebook configuration: maximum 50 epochs; image size 320; batch size 16; SGD with initial learning rate 0.005 and cosine schedule; weight decay 0.0005; patience 10; seed 42; deterministic mode enabled; AMP disabled; automatic augmentation disabled; random erasing 0.0. These values describe notebook settings; the exact checkpoint execution record was not available for independent verification.

## Experiment 02: family-aware cross-validation
The notebook maps collection sites to experiment-family identifiers and assigns each family wholly to one of three folds. One model is trained per fold, with a held-out test partition for each. Predictions from all three held-out partitions are pooled across 662 images to calculate aggregate metrics. Fold checkpoints remain distinct.

## Reported results
Pooled accuracy is 55.29% (366/662), balanced accuracy is 49.62%, and macro F1 is 0.4965. Fold test accuracies are 66.23% (n=231), 48.44% (n=192), and 50.21% (n=239). Majority-class accuracy is 48.79%. These figures are transcribed from project outputs and have not been recalculated from source prediction files in this repository.

The Experiment 02 scores apply only to its three fold-specific models. They do not describe the Experiment 01 full-run ONNX artifact.

## Reproduction requirements
Independent reproduction requires the source family manifest, split-generation code and seed, per-fold prediction files, checkpoint hashes, and software versions. The full-run ONNX artifact requires separate evaluation against its corresponding held-out test set.
