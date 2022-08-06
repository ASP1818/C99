import dropbox

class TransferData : 
    def __init__(self, access_token) :
        self.access_token = access_token


    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, "rb")
        dbx.file_upload(f.read(), file_to)

def main():
    access_token = "sl.BLTypFT_4CWVF6sGMgg0yZbyUHZSqRCI57kUyDvMknGBmDicR_7EvlVuGWncgJ2uYsyc2IZnDBKnJGLOej62amoJHHqEx0rNuzKSCbl7fsB3REhFlwTIDok4ZYI--_sHQgUF6_s"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path  to transfer: ")
    file_to = input("Enter the full path to dropbox:")

    transferData.upload_files(file_from, file_to)
    print("files has been moved successfully!!!")

main()
