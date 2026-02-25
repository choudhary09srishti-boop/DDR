AI DDR Builder



An AI-powered DDR (Detailed Diagnostic Report) generator that processes inspection and thermal reports to generate structured, client-friendly assessment reports.



🚀 Project Overview



This project builds an end-to-end AI workflow that:



\- Reads inspection and thermal PDF reports

\- Cleans and processes extracted text

\- Extracts structured information

\- Detects area-wise issues

\- Applies rule-based reasoning

\- Generates a structured DDR report

\- Explicitly handles missing or unclear information



The system avoids hallucination and only uses information present in the documents.



---



 Workflow Architecture



1\. \*\*PDF Ingestion\*\* – Load reports using `pypdf`

2\. \*\*Text Cleaning\*\* – Normalize extracted text

3\. \*\*Information Extraction\*\* – Extract structured fields

4\. \*\*Issue Detection\*\* – Detect dampness, tile hollowness, etc.

5\. \*\*Rule Engine\*\* – Assess severity and probable causes

6\. \*\*DDR Generation\*\* – Produce structured 7-section report

7\. \*\*Output Storage\*\* – Save final DDR to `/outputs`







 DDR Output Structure



The generated report contains:



1\. Property Issue Summary  

2\. Area-wise Observations  

3\. Probable Root Cause  

4\. Severity Assessment (with reasoning)  

5\. Recommended Actions  

6\. Additional Notes  

7\. Missing or Unclear Information  






 Handling Limitations



\- Thermal PDF appears image-based.

\- Structured temperature extraction is not available without OCR.

\- The system explicitly marks unavailable data as \*\*"Not Available"\*\*.

\- No facts are invented.






 Key Design Principles

\- No hallucinated data

\- Transparent reasoning

\- Client-friendly language

\- Modular \& scalable structure

\- Works on similar structured inspection reports











