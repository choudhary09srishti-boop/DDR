import re


def extract_basic_info(text):
    data = {}

    score = re.search(r"Complete Score\s*(\d+\.?\d*)%", text)
    if score:
        data["score"] = score.group(1)

    flagged = re.search(r"Flagged items\s*(\d+)", text)
    if flagged:
        data["flagged_items"] = flagged.group(1)

    age = re.search(r"Property Age.*?(\d+)", text)
    if age:
        data["property_age"] = age.group(1)

    floors = re.search(r"Floors:\s*(\d+)", text)
    if floors:
        data["floors"] = floors.group(1)

    date = re.search(r"Inspection Date.*?(\d{2}\.\d{2}\.\d{4})", text)
    if date:
        data["inspection_date"] = date.group(1)

    return data


def extract_thermal_info(text):
    data = {}

    temps = re.findall(r"(\d+\.\d+)\s*C", text)

    if not temps:
        data["status"] = "Thermal images attached. Structured temperature extraction not available."
        data["note"] = "Thermal PDF appears image-based. OCR required for precise temperature extraction."
        return data

    float_temps = list(map(float, temps))

    data["max_temperature"] = max(float_temps)
    data["min_temperature"] = min(float_temps)
    data["total_readings"] = len(float_temps)

    return data


def extract_issues(text):
    issues = []

    if "Dampness" in text:
        issues.append("Dampness observed in bedroom area")

    if "tile hollowness" in text.lower():
        issues.append("Tile hollowness observed in common bathroom")

    if not issues:
        issues.append("No major visible structural issues mentioned.")

    return issues
