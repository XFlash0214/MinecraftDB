from google.cloud import storage
import os
import datetime

class Imgmanager:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"
    client=storage.Client()
    bucket=client.get_bucket("piratedb-0214.appspot.com")
    imagepath="pirate2.gif"
    
    def Imgupload(
        imageBlob=bucket.blob("images/"+self.imagepath)
        imageBlob.upload_from_filename(self.imagepath)
        d=datetime.datetime(2040,1,1)
        self.url=imageBlob.generate_signed_url(d)
