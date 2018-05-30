# pythonであなたの欲しい本(epub/pdf)がサイトにあるかどうかクローリングする方法

python3はインストールされている前提
してないなら
Anacondaをインストールもしくは
```
brew install python3
```

## pythonで必要なライブラリをインストールする
```
./pip_install.sh
```

## 欲しい本のタイトルをざっくり入力する もしくは次のpython実行の引数に名前を指定する
(引数がない、もしくはエラーが生じた場合はtxtファイルにある本の名前を参照します)
```
vi title.txt
```

## クローリングの実行
```
python3 crawl.py XXX(XXXは任意:調べたい本の名前)
```
