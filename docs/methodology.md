# Experimental methodology

## Study question
Can image classification learn a coarse three-category turbidity label from images with measured FNU, with generalization assessed across experiment families?

## Dataset and preprocessing
The project notebook retrieves Turbidivision v1.0.0 and selects 662 images with usable FNU labels. It constructs project bands using low <5 FNU, moderate 5–<20 FNU, and high ≥20 FNU. Source images are converted to RGB, EXIF orientation is applied, resized to fit within 1024 × 1024 preserving aspect ratio, and saved as JPEG quality 92. Dataset credit and license are recorded in `dataset.md`.

## Two distinct experiments
**Experiment 01 full run** uses the site-separated train/validation/test dataset and writes `yolo26n_full_v1`. Its ONNX export is the artifact stored in `models/`. No verified test metrics for that exact artifact were supplied here.

**Experiment 02** maps site labels to experiment families and uses three family-aware held-out folds. Family groups remain together between folds to reduce leakage from related images. It trains three separate YOLO26n-cls checkpoints and combines their out-of-fold predictions to report the 662-image pooled results. The Experiment 02 metrics must not be attributed to the Experiment 01 ONNX model.

## Reported Experiment 02 results
Pooled accuracy 55.29% (366/662), balanced accuracy 49.62%, macro F1 0.4965. Test accuracy by fold: 66.23% (n=231), 48.44% (n=192), and 50.21% (n=239). The majority-class accuracy baseline is 48.79%. Values are transcribed from prior project outputs and were not recomputed in this workspace.

## Experiment 01 full-run settings in notebook
Pretrained `yolo26n-cls.pt`; maximum 50 epochs; image size 320; batch 16; device 0; workers 0; AMP disabled; SGD, initial learning rate 0.005, cosine schedule; weight decay 0.0005; no automatic augmentation; erasing 0.0; validation enabled; patience 10; seed 42; deterministic mode enabled. These settings are notebook configuration, not proof every setting was applied to the exact exported file.

## Reproducibility checklist
- Keep the original family manifest and split-generation code with the experiment records.
- Verify family IDs are disjoint between folds.
- Record the exact checkpoint hash, export command, and software versions for each artifact.
- Recalculate metrics from saved out-of-fold predictions before claiming independent reproduction.
- Evaluate the full-run ONNX artifact on its own untouched test set; do not substitute CV fold scores.
