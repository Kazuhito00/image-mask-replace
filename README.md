# image-mask-replace
　image-mask-replaceはマスク画像を用いて2枚の画像を合成するプログラムです。
 
　学習データのデータ拡張を目的に作成しました。

　[hsv-mask-extracter](https://https://github.com/Kazuhito00/hsv-mask-extracter)で作成したマスク画像を利用できます。

# Requirement
 
* OpenCV 3.4.2(or later)
 
# Installation
 
ディレクトリを丸ごとコピーして実行してください。
 
# Usage
 
サンプルの実行方法は以下です。
 
```bash
python image_mask_replace.py
```

以下のコマンドラインオプションがあります。

--width：合成後の画像サイズ(幅)

--height：合成後の画像サイズ(高さ)

--original：合成前の画像を保存するか(True/False)

・capture/image
　→オリジナル画像

・capture/mask
　→オリジナル画像に対するマスク画像

・capture/replace
　→差し替え画像

・capture/output
　→合成後ファイル格納先


# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
cvoverlayimg is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

また、サンプルの差し替え画像は[フリー素材ぱくたそ](https://www.pakutaso.com)様の写真を利用しています。
