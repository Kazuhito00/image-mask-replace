# image-mask-replace
　image-mask-replaceはマスク画像を用いて2枚の画像を合成するプログラムです。
 
　学習データのデータ拡張を目的に作成しました。

　[hsv-mask-extracter](https://https://github.com/Kazuhito00/hsv-mask-extracter)で作成したマスク画像を利用できます。

# Requirement
 
* OpenCV 3.4.2(or later)
 
# Installation
 
ディレクトリを丸ごとコピーして実行してください。

・capture/image

　→オリジナル画像
 
![00001](https://user-images.githubusercontent.com/37477845/77141041-de0dd380-6abe-11ea-8bb4-9db4a9c6275e.png)


・capture/mask

→オリジナル画像に対するマスク画像

![00001](https://user-images.githubusercontent.com/37477845/77141042-e108c400-6abe-11ea-8e64-069606f4ff48.png)

・capture/replace

→差し替え画像

![005KZ1123FOTO_TP_V4](https://user-images.githubusercontent.com/37477845/77141047-e403b480-6abe-11ea-84f4-1958090452ef.jpg)

・capture/output

→合成後ファイル保存先

![00001_001](https://user-images.githubusercontent.com/37477845/77141051-e6fea500-6abe-11ea-9a9e-a5deb7ab1af3.png)
 
# Usage
 
サンプルの実行方法は以下です。
 
```bash
python image_mask_replace.py
```

以下のコマンドラインオプションがあります。

--width：合成後の画像サイズ(幅)

--height：合成後の画像サイズ(高さ)

--original：合成前の画像を保存するか(True/False)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
image-mask-replace is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

また、サンプルの差し替え画像は[フリー素材ぱくたそ](https://www.pakutaso.com)様の写真を利用しています。
