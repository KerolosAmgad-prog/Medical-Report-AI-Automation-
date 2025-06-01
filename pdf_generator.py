
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(all_patients_data, predictions, output_file):
    all_patients_data = all_patients_data.reset_index(drop=True)  # Ensure proper indexing
    total_patients = min(len(all_patients_data), len(predictions))  # Match predictions

    print(f"Generating PDF for {total_patients} patients")

    c = canvas.Canvas(output_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 780, "Dialysis Prediction Report - All Patients")

    y_position = 760

    for index in range(total_patients):  # Loop within valid bounds
        patient_data = all_patients_data.iloc[index]  # Get correct row
        print(f"Processing patient {index + 1}")

        if y_position < 100:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = 780

        c.drawString(100, y_position, f"Patient {index + 1}")
        y_position -= 20

        for key, value in patient_data.items():
            value = "N/A" if pd.isna(value) else value
            c.drawString(100, y_position, f"{key.capitalize()}: {value}")
            y_position -= 20

        # Add predictions safely
        bp_pred, temp_pred, flow_pred = predictions[index]
        c.drawString(100, y_position, f"Predicted Post-Dialysis BP: {bp_pred}")
        y_position -= 20
        c.drawString(100, y_position, f"Predicted Post-Dialysis Temp: {temp_pred}")
        y_position -= 20
        c.drawString(100, y_position, f"Recommended Blood Flow Rate: {flow_pred}")
        y_position -= 30

    c.save()
    print(f"PDF successfully generated: {output_file}")
