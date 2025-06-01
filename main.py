

from Model import train_models, predict,load_data ,preprocess_data
from pdf_generator import generate_pdf
from whatsapp import send_whatsapp
from google_drive import upload_to_google_drive
from send_Email import send_email_with_pdf

def main():
    try:
        # Step 1: Load and preprocess data
        data = load_data("patient_data.csv")
        X_train, X_test, y_bp_train, y_bp_test, y_temp_train, y_temp_test, y_flow_train, y_flow_test = preprocess_data(data)
        print("Data loaded and preprocessed successfully!")

        X_test = X_test.reset_index(drop=True)

        # Debugging: Check test data sizes
        print(f"X_test shape: {X_test.shape}")  # Check test data size
        print(f"y_bp_test shape: {y_bp_test.shape}")  # Expected test labels
        print(f"y_temp_test shape: {y_temp_test.shape}")
        print(f"y_flow_test shape: {y_flow_test.shape}")

        # Step 2: Train models
        bp_model, temp_model, flow_model = train_models(X_train, y_bp_train, y_temp_train, y_flow_train)
        print("Models trained successfully!")

        # Step 3: Generate predictions for all test data
        predictions = []
        for i, (_, row) in enumerate(X_test.iterrows()):
            try:
                result = predict(bp_model, temp_model, flow_model, row.to_frame().T)
                if len(result) == 3:
                    predictions.append(result)
                else:
                    print(f"Warning: Unexpected output from predict() for index {i}: {result}")
            except Exception as e:
                print(f"Error predicting for patient {i}: {e}")


        # Debugging: Check the number of predictions
        print(f"Total patients in X_test: {len(X_test)}")
        print(f"Total predictions generated: {len(predictions)}")


        # step 4 ; pdf generator
        pdf_file = "dialysis_report_all_patients.pdf"
        generate_pdf(X_test, predictions, pdf_file)
        print(f"PDF generated: {pdf_file}")



      # Step 5: Upload PDF to Google Drive and get the public URL

        pdf_url = upload_to_google_drive(pdf_file)

        if pdf_url:
            print(f"File uploaded successfully! Public URL: {pdf_url}")
        else:
            print("File upload failed.")


        # Step 6: Send PDF via WhatsApp
        send_whatsapp(
            receiver_phone="+201027033593",  # Replace with recipient's phone number
            message="Hi, please find attached the Dialysis Prediction Report.",
            media_url=pdf_file
        )
        print("WhatsApp message sent successfully!")
    #step 6 send the file to Email
        send_email_with_pdf(
            receiver_email="mario.labib663@gmail.com",
            subject="Dialysis Prediction Report",
            body="Please find attached your dialysis prediction report.",
            pdf_path=pdf_file
        )


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()