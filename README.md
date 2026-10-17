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

