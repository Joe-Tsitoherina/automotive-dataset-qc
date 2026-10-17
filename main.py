
import json
from pathlib import Path

# 1. Define the project folders
PROJECT_FOLDER = Path(__file__).resolve().parent
DATASET_FOLDER = PROJECT_FOLDER / "dataset"
IMAGES_FOLDER = DATASET_FOLDER / "images"
LABELS_FOLDER = DATASET_FOLDER / "labels"

REPORT_PATH = PROJECT_FOLDER / "sample_report.json"

# 2. Define the supported image extensions
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def main():
    # 3. Validate both folders before starting QC
    if not IMAGES_FOLDER.is_dir():
        print(f"ERROR: Images folder not found: {IMAGES_FOLDER}")
        return

    if not LABELS_FOLDER.is_dir():
        print(f"ERROR: Labels folder not found: {LABELS_FOLDER}")
        return

    # 4. Collect image and annotation filenames
    image_files = [
        file for file in IMAGES_FOLDER.iterdir()
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    label_files = [
        file for file in LABELS_FOLDER.iterdir()
        if file.is_file()
        and file.suffix.lower() == ".json"
    ]

    # 5. Extract filename stems
    image_stems = {file.stem for file in image_files}
    label_stems = {file.stem for file in label_files}

    # 6. Compare images and labels
    matching_pairs = image_stems & label_stems
    missing_annotations = image_stems - label_stems
    extra_annotations = label_stems - image_stems

    # 7. Determine the QC status
    qc_status = (
        "PASS"
        if not missing_annotations and not extra_annotations
        else "FAIL"
    )

    # 8. Build the QC report
    report = {
        "total_images": len(image_files),
        "total_labels": len(label_files),
        "matching_pairs": len(matching_pairs),
        "missing_annotations": sorted(missing_annotations),
        "extra_annotations": sorted(extra_annotations),
        "qc_status": qc_status,
    }

    # 9. Save the report as valid JSON
    with REPORT_PATH.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=4)

    # 10. Display the results
    print("AUTOMOTIVE DATASET QC REPORT")
    print(json.dumps(report, indent=4))

    print("\nMissing annotations:")
    for stem in sorted(missing_annotations):
        print(f" - {stem}")

    print("\nExtra annotations:")
    for stem in sorted(extra_annotations):
        print(f" - {stem}")

    print(f"\nQC Status: {qc_status}")
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
