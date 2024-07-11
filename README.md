# GIF to Sprite Sheet Converter

このPythonスクリプトは、指定された入力ディレクトリ`in`内のすべてのGIFファイルをスプライトシートに変換し、指定された出力ディレクトリ`out`に保存します。

## セットアップ

1. リポジトリをクローンします。

    ```bash
    git clone <リポジトリのURL>
    cd <リポジトリのディレクトリ>
    ```

2. `pipenv`を使用して環境をセットアップします。

    ```bash
    pipenv install
    ```

## 使い方

1. `in`ディレクトリに処理したいGIFファイルを配置します。
2. 以下のコマンドを実行してスクリプトを実行します。

    ```bash
    pipenv run python main.py
    ```

3. スプライトシートは`out`ディレクトリに出力されます。