from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import  os
#from google.oauth2 import service_account
#from googleapiclient.discovery import build
#from googleapiclient.http import MediaFileUpload
# Path to your client secrets JSON file
CLIENT_SECRET_FILE = "D:\Hemodialysis\machine learning and testing\Whatsapp sending messsage\client_secret_167774620994-579s4vopr9dii0afnojflhdsshl2d28k.apps.googleusercontent.com.json"


def authenticate_drive():
    """Authenticate and return Google Drive instance."""
    gauth = GoogleAuth()

    # Ensure the client secrets file exists
    if not os.path.exists(CLIENT_SECRET_FILE):
        raise FileNotFoundError(f"Client secrets file not found: {CLIENT_SECRET_FILE}")

    # Load client config and authenticate
    gauth.LoadClientConfigFile(CLIENT_SECRET_FILE)
    gauth.LocalWebserverAuth()

    return GoogleDrive(gauth)


def upload_to_google_drive(file_path):
    """Uploads a file to Google Drive and returns a direct download link."""
    drive = authenticate_drive()

    gfile = drive.CreateFile({'title': os.path.basename(file_path)})
    gfile.SetContentFile(file_path)
    gfile.Upload()

    # Make the file public
    gfile.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})

    # Generate a direct download link
    direct_link = f"https://drive.google.com/uc?export=download&id={gfile['id']}"

    return direct_link


# Example Usage
if __name__ == "__main__":
    file_path = "example.pdf"  # Replace with your actual file path
    download_link = upload_to_google_drive(file_path)
    print("Direct Download Link:", download_link)
