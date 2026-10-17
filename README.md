# Automotive Dataset QC

## Project Overview

This is a learning project developed as part of my journey toward becoming a Computer Vision Data Specialist.

The goal is to check the consistency between automotive image files and their corresponding annotation files using Python.

## Problem

A dataset may contain:
- Images without corresponding annotation files
- Annotation files without corresponding images
- Image-label filename mismatches

These inconsistencies need to be identified before the dataset is used in a computer vision workflow.

## Current Features

- Inspect image and label folders
- Extract filenames using `pathlib`
- Compare image and annotation filenames using `.stem`
- Identify missing annotations
- Identify extra annotation files
- Generate a Dataset QC summary

## Technologies

- Python
- pathlib
- JSON
- GitHub

## Example Dataset Structure

```text
dataset/
├── images/
│   ├── car_001.jpg
│   ├── car_002.jpg
│   └── car_003.jpg
└── labels/
    ├── car_001.json
    ├── car_003.json
    └── car_004.json
```

## Expected QC Findings

- Matching pairs: 2
- Missing annotations: 1 (`car_002`)
- Extra annotation files: 1 (`car_004`)

The expected result is `FAIL` because inconsistencies were detected.

## Learning Objectives

This project helps me develop practical skills in Python programming, dataset inspection, file validation, and automotive Dataset QC.

## Project Status

Learning project — under development.

Additional validation rules and automated reporting will be added as the project progresses.

## How to Run

### Requirements

- Python 3.10 or later
- No third-party packages required

### Dataset Structure

Place the dataset in the following structure:

```text
dataset/
├── images/
└── labels/
```

Image and annotation filenames must share the same stem. For example, `car_001.jpg` corresponds to `car_001.json`.

### Run the QC Script

From the project root, run:

```bash
python main.py
```

The script checks image-label filename consistency and generates `sample_report.json`.

## Test Results

The sample test dataset contains three image files and three JSON annotation files.

| Metric | Result |
|---|---:|
| Total images | 3 |
| Total labels | 3 |
| Matching pairs | 2 |
| Missing annotations | 1 |
| Extra annotation files | 1 |
| QC status | FAIL |

The test detects the missing annotation for `car_002` and the extra annotation file `car_004.json`.

See `sample_report.json` for the example output.

## Current Limitations

- Checks filename consistency only.
- Does not validate JSON contents or annotation schemas.
- Does not verify image readability.
- Does not evaluate segmentation masks or polygons.
- Uses a small synthetic test dataset.

## Learning Outcomes

This project demonstrates practical use of Python `pathlib`, sets, loops, conditional statements, JSON serialization, and basic Dataset QC reporting.

**Project status:** Learning project — first functional version.
