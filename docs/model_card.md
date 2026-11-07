# Model card: WaterVision AI YOLO26n-cls

## Summary
Experimental image classifier for assigning one of three study-specific turbidity categories to images. The study record reports three-fold family-aware validation on 662 Turbidivision images, pooled accuracy 55.29%, balanced accuracy 49.62%, and macro F1 0.4965.

## Intended use
Educational demonstration and research into image-based turbidity classification under controlled experimental conditions.

## Out of scope
The model does not assess drinking-water potability, pathogens, chemical contamination, regulatory compliance, or field safety. It must not be used to approve or reject water for drinking or other safety decisions.

## Data and evaluation
Data provenance and license remain unverified. Three family-aware folds were reported; fold test accuracies varied from 48.44% to 66.23%. The pooled score is the appropriate summary, not the best fold or best validation score.

## Limitations
- Modest performance, only 6.50 percentage points above the reported majority-class accuracy baseline.
- Performance varies by held-out experiment family.
- The model may learn lighting, container, background, camera, or acquisition conditions rather than turbidity alone.
- Exact class thresholds, calibration, external validation, subgroup analysis, and field testing have not been verified.
- Checkpoint identity, hashes, training configuration, and software versions are unavailable here.

## Risks and mitigations
A confident prediction can still be wrong, including underestimating high turbidity. Always use a calibrated turbidity instrument for measurement and follow applicable water-testing procedures. Do not translate model categories into a safety judgment.

## Artifact details
No weights are bundled. The project record references a distinct fold 2 `best.pt` checkpoint in Drive; it must be retrieved and validated before distribution. Do not present it as a single model trained across all folds.
