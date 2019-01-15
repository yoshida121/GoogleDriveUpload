# GoogleDriveUpload
File upload to Google drive by Python.

# 実行環境
- Anaconda3 (Python3.6)
- Windows Server 2016
- VSCode

# 必要なもの
- Googleアカウント
- インターネット環境

# 事前準備
PyDriveのインストール(PythonからGoogleDriveを操作するモジュール)  
- Anacondaの場合
`conda install -c conda-forge pydrive`
- pipの場合
`(sudo) pip3 install pydrive google-api-python-client`

# Google Cloud Platformからアクセスキーの取得
<https://console.developers.google.com/apis/>にアクセス  
OAuthクライアントIDとクライアントシークレットを作成(詳しいことは検索してください)  
  
次にクライアントIDとシークレットIDをGoogleCloudPlatformからjsonでダウンロードしてclient_secrets.jsonにファイル名の変更  
本リポジトリをcloneしたフォルダ内に配置してください 
  
- ファイル構成  
GoogleDriveUpload  
|-- GoogleDriveUpload.py  
|-- settings.yaml  
|-- client_secrets.json  

# Google Drive APIの有効化
ここも詳しくは検索してください。時間が出来ましたら書きます。

# settings.yamlに追加
settings.yamlをエディタ(VSCode)で開きます  
<クライアントID>にはGoogleCloudPlatformから取得したクライアントID  
<クライアントシークレット>にはクライアントシークレットに置き換える

# 残りはsample.ipynbの通りに実行

