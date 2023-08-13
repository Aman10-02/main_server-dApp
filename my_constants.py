from flask import Flask

# UPLOAD_FOLDER = 'C:/Users/Aman/Desktop/Blockchain-based-Decentralized-File-Sharing-System-using-IPFS/main_server/uploads'
# DOWNLOAD_FOLDER = 'C:/Users/Aman/Desktop/Blockchain-based-Decentralized-File-Sharing-System-using-IPFS/main_server/downloads'
UPLOAD_FOLDER = '/uploads'
DOWNLOAD_FOLDER = '/downloads'

app = Flask(__name__)
app.config['KEY'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDhGNWNmMjczYzY1YjQ0ZmFCNzMyOGUwM2U0YkZGNEQ5RTg4NEE5YjMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2OTE5MjU2NDI4ODQsIm5hbWUiOiJkZWNlbnRyYWxpemVkRmlsZVNoYXJlIn0.rf7Jv5bCAvr06If4AX5ptIfIOxD-2RUx6PnLeFNK0zk"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
