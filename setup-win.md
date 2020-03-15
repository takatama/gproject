# Windows セットアップ方法

Windows 10 Home 64 bit を使ってセットアップする方法を説明する。

## GitHub
- GitHub のアカウントがなければ作成する。
- gproject を Fork する。
  - https://github.com/midododoka/gproject で Fork ボタンを押す。

## GitHub Desktop
- https://desktop.github.com/ からインストールして、GitHub にサインインする。
- Fork した gproject を clone する。
  - %HOMEPATH%\OneDrive\ドキュメント\GitHub\gproject 

## Python
- インストール
  - 検索窓に python と入力して、python をインストールする。
  - 検索窓に cmd と入力してターミナルを起動する。
    - python -V と入力して python がインストールされて動作することを確認する。
    - pip -h と入力してパッケージ管理 pip がインストールされて動作することを確認する。
  - 必要なパッケージをインストールする
    - ターミナルで以下のコマンドを入力する
      - cd %HOMEPATH%\OneDrive\ドキュメント\GitHub\gproject と入力する。
      - pip install -r requirements.txt
    - Successfully installed Click-7.0... と表示されたら OK。
- Flask 実行
  - ターミナルで以下のコマンドを入力する。
    - python app.py
  - 「このアプリの機能のいくつかが Windows Defender ファイアウォールでブロックされています」と表示される
    - プライベート ネットワーク、をチェックする。
    - パブリック ネットワーク、のチェックを外す！！！
    - アクセスを許可する。
    -  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) と表示されたら OK。
  - ブラウザーで http://127.0.0.1:5000/ にアクセスする
    - 0.0.0.0:5000 ではつながらないので注意！！

## Visual Studio Code
- インストール
  - https://code.visualstudio.com/docs/setup/windows に従ってインストールする。

