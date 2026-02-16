import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

SAMPLE_REPORT_PATH = "data/Sample Report.pdf"
THERMAL_REPORT_PATH = "data/Thermal Images.pdf"

OUTPUT_PATH = "outputs/final_ddr.txt"
