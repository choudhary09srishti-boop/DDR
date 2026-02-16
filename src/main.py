from config import SAMPLE_REPORT_PATH, THERMAL_REPORT_PATH
from pdf_loader import load_pdf
from cleaner import clean_text
from extractor import (
    extract_basic_info,
    extract_thermal_info,
    extract_issues,
)
from rule_engine import (
    assess_severity,
    probable_root_cause,
    recommended_actions,
)


def main():
    # Load sample report
    sample_raw = load_pdf(SAMPLE_REPORT_PATH)
    sample_clean = clean_text(sample_raw)

    basic_info = extract_basic_info(sample_clean)
    issues = extract_issues(sample_clean)

    # Load thermal report
    thermal_raw = load_pdf(THERMAL_REPORT_PATH)
    thermal_clean = clean_text(thermal_raw)
    thermal_info = extract_thermal_info(thermal_clean)

    # Rule Engine
    severity, reasoning = assess_severity(basic_info, issues)
    causes = probable_root_cause(issues)
    actions = recommended_actions(issues)

    print("Basic Info:", basic_info)
    print("\nIssues:", issues)
    print("\nSeverity:", severity)
    print("Reasoning:", reasoning)
    print("\nProbable Causes:", causes)
    print("\nRecommended Actions:", actions)
    print("\nThermal Info:", thermal_info)

    # Build DDR text
    ddr_text = ""
    ddr_text += "================ DDR REPORT ================\n\n"

    ddr_text += "1. Property Issue Summary\n"
    ddr_text += f"The inspection score is {basic_info.get('score', 'Not Available')}%.\n"
    ddr_text += f"Flagged items: {basic_info.get('flagged_items', 'Not Available')}.\n\n"

    ddr_text += "2. Area-wise Observations\n"
    for issue in issues:
        ddr_text += f"- {issue}\n"
    ddr_text += "\n"

    ddr_text += "3. Probable Root Cause\n"
    for cause in causes:
        ddr_text += f"- {cause}\n"
    ddr_text += "\n"

    ddr_text += "4. Severity Assessment\n"
    ddr_text += f"Severity Level: {severity}\n"
    for r in reasoning:
        ddr_text += f"- {r}\n"
    ddr_text += "\n"

    ddr_text += "5. Recommended Actions\n"
    for action in actions:
        ddr_text += f"- {action}\n"
    ddr_text += "\n"

    ddr_text += "6. Additional Notes\n"
    ddr_text += "Thermal images were attached to the report.\n\n"

    ddr_text += "7. Missing or Unclear Information\n"
    if "status" in thermal_info:
        ddr_text += "- Structured thermal temperature data: Not Available\n"
    else:
        ddr_text += "- Thermal data processed successfully\n"

    ddr_text += "\n============================================\n"

    # Save to file
    with open("outputs/final_ddr.txt", "w", encoding="utf-8") as f:
        f.write(ddr_text)

    print("DDR Report saved to outputs/final_ddr.txt")

if __name__ == "__main__":
    main()
