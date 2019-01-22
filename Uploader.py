# coding: utf-8
# (C) 2019 yoshida121. All rights reserved.


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

class GoogleDriveUpload():
    """ PythonからGoogleDriveへとファイルをアップロードする """
    def __init__(self, child_folder=None):
        """
        Parameters:
            child_folder : 子ディレクトリに認証ファイルが存在する場合に指定
        """
        if child_folder is not None:
            os.chdir("./" + str(child_folder) + "/")
        auth = GoogleAuth()
        auth.CommandLineAuth()
        # print(os.getcwd)
        self.drive = GoogleDrive(auth)
        if child_folder is not None:
            os.chdir("./../")

    def get_folder_id(self, file_name, parents_fold=None):
        """
        GoogleDriveから指定のフォルダ(ファイル)IDを取得する

        Parameters:
            file_name : 取得したいファイル名
            parents_fold : 取得するIDの親ディレクトリを指定(いつか実装する)

        Returns:
            folder_idx : 取得したフォルダIDのリスト 
        """
        folder_idx = []
        base_query = "trashed=false"
        if parents_fold is not None:
            add_query = "{} in parents and".format(parents_fold)
        else:
            add_query = ""
        
        for file_list in self.drive.ListFile({"q": add_query + base_query}):
            for file in file_list:
                if file["title"] == file_name:
                    folder_idx.append(file["id"])
        return folder_idx
        
    def upload(self, file_name, mime=None, fold_upload=False, parents_id=None, print_data=False):
        """
        ファイルをGoogleDriveへとアップロードする

        Parameters:
            file_name : アップロードするファイル名
            print_data : アップロードしたファイルのファイル名とIDを取得する
        """

        if file_name.endswith('.csv'):  
            # 自身の環境に合わせてmimeTypeを増やしてください. 下記のURLにMIMEの一覧あり
            # http://www.geocities.co.jp/Hollywood/9752/mime.html
            # https://developers.google.com/drive/api/v3/mime-types
            mimeType = "text/csv"
        elif file_name.endswith('.ipynb'):
            mimeType = 'application/vnd.google.colaboratory'
        elif fold_upload:
            mimeType = "application/vnd.google-apps.folder"
        else:
            mimeType = None

        if mime is not None:
            mimeType = mime

        if fold_upload:
            title, id =  self.upload(file_name, print_data=True, mime=mimeType)
            print(id)
            os.chdir(file_name)
            up_file_list = os.listdir()
            for up_file in up_file_list:
                temp_title, temp_id = self.upload(up_file, print_data=True, parents_id=id)
            os.chdir("../")
            return 
    
        if parents_id is None:
            parents_id = "root"
        
        # print(mimeType)
        file = self.drive.CreateFile({"title": file_name, "mimeType": mimeType, "parents": [{"id": parents_id}]})
        print("Uploadeing...")
        file.Upload()
        print("Complete!")
        if print_data:
            print("-------------------------------")
            print("File Name :", file["title"])
            print("File ID :", file["id"])
            print("-------------------------------")
            return file["title"], file["id"]

