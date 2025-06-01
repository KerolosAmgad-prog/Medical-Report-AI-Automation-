import smtplib
import os
from email.message import EmailMessage

def send_email_with_pdf(receiver_email, subject, body, pdf_path):
    sender_email = "kerolosamgad200@gmail.com"  # 🔹 Replace with your email
    sender_password = "202001067"  # 🔹 Replace with your App Password

    # Create the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach the PDF file
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
            msg.add_attachment(pdf_data, maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))

        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

