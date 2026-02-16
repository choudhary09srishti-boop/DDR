def assess_severity(basic_info, issues):
    severity = "Low"
    reasoning = []

    flagged = int(basic_info.get("flagged_items", 0))
    age = int(basic_info.get("property_age", 0))

    if flagged > 0:
        severity = "Moderate"
        reasoning.append("Inspection report shows flagged items.")

    if "Dampness observed in bedroom area" in issues:
        severity = "Moderate"
        reasoning.append("Dampness may indicate water seepage risk.")

    if age > 10:
        reasoning.append("Property age suggests possible wear and tear factors.")

    return severity, reasoning


def probable_root_cause(issues):
    causes = []

    if any("Dampness" in issue for issue in issues):
        causes.append("Possible water seepage or plumbing leakage.")

    if any("Tile hollowness" in issue for issue in issues):
        causes.append("Improper tile installation or adhesive failure.")

    if not causes:
        causes.append("No major structural root cause identified.")

    return causes


def recommended_actions(issues):
    actions = []

    if any("Dampness" in issue for issue in issues):
        actions.append("Inspect plumbing lines and waterproofing in affected area.")

    if any("Tile hollowness" in issue for issue in issues):
        actions.append("Re-fix or replace affected tiles after surface inspection.")

    if not actions:
        actions.append("Routine maintenance recommended.")

    return actions