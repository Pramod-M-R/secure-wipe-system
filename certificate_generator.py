from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generate_certificate(filename, score, level, prediction):
    file_name_only = os.path.basename(filename)

    # Save in project folder
    pdf_path = os.path.join(os.getcwd(), "certificate.pdf")

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("SECURE DATA WIPE CERTIFICATE", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"File: {file_name_only}", styles['Normal']))
    content.append(Paragraph(f"Date: {datetime.now()}", styles['Normal']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Verification Results:", styles['Heading2']))
    content.append(Paragraph(f"Recoverability Score: {score}", styles['Normal']))
    content.append(Paragraph(f"Security Level: {level}", styles['Normal']))
    content.append(Paragraph(f"Prediction: {prediction}", styles['Normal']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Status: SUCCESSFULLY WIPED", styles['Normal']))

    doc.build(content)

    print(f"\n📄 Certificate saved at:\n{pdf_path}")

    # 🔥 AUTO OPEN PDF
    try:
        os.startfile(pdf_path)
    except:
        print("⚠️ Could not auto-open PDF")