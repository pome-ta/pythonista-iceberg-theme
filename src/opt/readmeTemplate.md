# pythonista-iceberg-theme

Editor color theme for [Pythonista for iOS](https://omz-software.com/pythonista/).

Original [iceberg.vim](https://github.com/cocopon/iceberg.vim) (reference: [cocopon/vscode-iceberg-theme](https://github.com/cocopon/vscode-iceberg-theme)) for Vim by [cocopon (Hiroki Kokubun)](https://github.com/cocopon).

![screenshot](./screenshot/screenshot.png)

> [!WARNING]
> Use at your own risk! User themes aren't "officially" supported, and this may break in future versions.
> If you enter invalid JSON or anything else that the app can't deal with, it _will_ crash -- your input is not validated in any way.  
> 自己責任で使用してください。ユーザーテーマは "公式に "サポートされていませんので、将来のバージョンでは壊れるかもしれません。 無効な JSON やアプリが処理できないものを入力すると、クラッシュします。

## How to Install

On your device, "`| Tap on this Link |`". If Pythonista 3 is installed, it will ask you to open the app. Tap `Open` to install it.  
**Or**, copy the string displayed in "URL scheme raw", display it as a hyperlink on Pythonista3, and tap it.

Pythonista3 がインストールされているデバイスで、「`| Tap on this Link |`」 をタップ。「"Pythonista"で開きますか?」の表示で、「開く」を選択。  
**または、**「URL scheme raw」の文字列をコピー。Pythonista3 等で、ハイパーリンク形式にして開く。

{{ section }}

## Building your own

> [!CAUTION]
> URL のリンク、scheme よりインストールした theme ファイル名: UUID（のような）形式  
> 以下のコードから生成した theme ファイル名: 取得先の`.json` 名  
> と、ファイル名が異なります


### 生成反映：`applytheme.py`

[`./src/applytheme.py`](https://github.com/pome-ta/pythonista-iceberg-theme/blob/main/src/applytheme.py)

- 参照先のリポジトリからデータを取得
  - theme の`.json` と、リポジトリ情報を統合
  - 統合したデータを`.json` 形式で dump
    - `.src/opt/VSCodeThemeDumps` へ格納(`.gitignore`)
- Pythonista3 の theme 形式へ変換(`.json`)
- 変換したものを格納
  - Pythonista3 内`userThemesPath`
  - `./theme`
- `README.md` 書き換え
  - URL scheme を生成
    - `.json` を`zlib` で圧縮、`base64` で decode
  - URL scheme を[TinyURL](https://tinyurl.com/) で短縮
    - URL scheme を、Markdown 上でリンク認識させるため

### 修正確認：`browsePA2UIThemePath.py`

[`./src/browsePA2UIThemePath.py`](https://github.com/pome-ta/pythonista-iceberg-theme/blob/main/src/browsePA2UIThemePath.py)

- Pythonista3 上で User Theme として認識されているディレクトリを表示
- 通常通りの操作が可能
  - 閲覧編集
  - リネーム
  - 削除

