import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('drive', 'v3', credentials=creds)

folder_id = '1ozPL7dy5rbS-mG8Ai4DPCwk0J8H0jpBo'

results = service.files().list(
    q=f"'{folder_id}' in parents", fields="files(id, name)"
).execute()

files = results.get('files', [])

if not files:
    raise FileNotFoundError('No files found.')
else:
    output_dir = '../../curriculos'
    os.makedirs(output_dir, exist_ok=True)

    print('Files:')
    for file in files:
        print(f"{file['name']} ({file['id']})")

        request = service.files().get_media(fileId=file['id'])
        file_path = os.path.join(output_dir, file['name'])
        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")
