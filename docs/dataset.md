# Dataset provenance, attribution, and license

## Source and credit

The supplied Colab notebook downloads the upstream Turbidivision GitHub release tagged `v1.0.0` from `YellowTeamRobot/AI_Turbidity_Honors2023-4`. It reads the official master label table and image archives, then keeps the 662 images with usable FNU labels for this project.

The cited source dataset is:

> Rudy, I. M., & Wilson, M. J. (2024). *Underwater Image/Turbidity Dataset* (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10951021

Zenodo's record metadata identifies the dataset license as **AGPL-3.0-or-later**. The upstream project repository also declares AGPL-3.0. Preserve the dataset citation and license notice in any permitted redistribution. This repository does not include the raw images or a derived dataset archive.

Related paper:

> Rudy, I. M., & Wilson, M. J. (2024). Turbidivision: a machine vision application for estimating turbidity from underwater images. *PeerJ, 12*, e18254. https://doi.org/10.7717/peerj.18254

The paper is distributed under CC BY 4.0. That license applies to the paper; do not treat it as a substitute for the separate dataset record's AGPL-3.0-or-later license.

## Project labels and transformation

The notebook first uses the source's published fine-grained FNU bins for auditing, then creates three project classes from measured FNU:

- `low`: FNU < 5
- `moderate`: 5 ≤ FNU < 20
- `high`: FNU ≥ 20

Images are converted to RGB, EXIF orientation is applied, resized to fit within 1024 × 1024 while preserving aspect ratio, and saved as JPEG (quality 92). The repository does not publish those transformed images. For Experiment 02, groups were mapped to experiment families and held together across three folds.

## Redistribution and limitations

The notebook's source identifies the upstream repository and release, while the Zenodo dataset record declares AGPL-3.0-or-later. Keep the source notices and citation with any distribution. The dataset is not bundled here. No independent image-by-image rights audit was performed; if a source image contains third-party material or separate restrictions, those may still apply. Do not relicense the data under MIT or CC BY based solely on the paper license.
