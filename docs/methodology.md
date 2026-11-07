# Experimental methodology

## Study question
Can image classification learn a coarse three-category turbidity label from the 662 labeled Turbidivision images, with generalization assessed across experiment families?

## Data and grouping
The conversation record reports 662 images and 13 independent family groups. Cross-validation was family-aware: image families were kept together when assigning folds to reduce leakage between related experimental images. The exact manifest and split-generation implementation were not available for this handoff and must be checked before claiming exact reproduction.

## Model and evaluation
Architecture: YOLO26n-cls. Three folds were trained and evaluated on held-out images. Pooled out-of-fold predictions gave 366 correct of 662 (55.29%) accuracy, 49.62% balanced accuracy, and 0.4965 macro F1. Fold test accuracies were 66.23%, 48.44%, and 50.21%, with n=231, 192, and 239 respectively. The unweighted majority-class baseline was 48.79%.

## Interpretation
The modest pooled improvement over majority-class accuracy and variation among folds indicate weak and unstable generalization across families. Validation performance, including a reported 91.11% for fold 2, is not a substitute for held-out test performance. The result supports a proof-of-concept conclusion only.

## Reproduction checklist
- Recover and audit the original notebook and Drive manifest.
- Confirm exact FNU class boundaries and class counts.
- Confirm family IDs are preserved and disjoint between train, validation, and test within each fold.
- Record seeds, image size, batch size, epochs, optimizer, augmentation, pretrained weights, stopping criteria, package versions, hardware, and checkpoint hashes.
- Regenerate pooled predictions from the three appropriate held-out fold checkpoints and calculate metrics once per image.
- Keep exploratory choices separate from final held-out evaluation.
