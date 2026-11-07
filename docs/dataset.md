# Dataset provenance and attribution

## Source

The supplied Colab notebook downloads the `v1.0.0` release from [YellowTeamRobot/AI_Turbidity_Honors2023-4](https://github.com/YellowTeamRobot/AI_Turbidity_Honors2023-4). It reads the master label table and image archives and selects 662 images with usable FNU labels.

## Dataset citation

Rudy, I. M., & Wilson, M. J. (2024). *Underwater Image/Turbidity Dataset* (1.0.0) [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.10951021](https://doi.org/10.5281/zenodo.10951021).

The Zenodo record metadata declares AGPL-3.0-or-later. The upstream project repository also declares AGPL-3.0. Raw images and derived image archives are not included in this repository.

## Related publication

Rudy, I. M., & Wilson, M. J. (2024). Turbidivision: a machine vision application for estimating turbidity from underwater images. *PeerJ, 12*, e18254. [https://doi.org/10.7717/peerj.18254](https://doi.org/10.7717/peerj.18254). The article is published under CC BY 4.0. This publication license is distinct from the dataset record's license.

## Label mapping and preprocessing

The project maps source FNU labels into three classes: low (<5 FNU), moderate (5 to <20 FNU), and high (≥20 FNU). Images are converted to RGB with EXIF orientation applied, resized within 1024 × 1024 pixels while preserving aspect ratio, and saved as JPEG at quality 92. Experiment 02 assigns mapped experiment families to separate CV folds.

The dataset record and upstream repository provide the applicable source terms. No independent item-level rights audit was performed for material embedded in individual images.
