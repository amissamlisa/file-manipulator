# File Manipulator
ファイルの操作が出来るツールです

## コマンド一覧

### reverse
指定した入力ファイルパスの中にあるファイルの内容を逆にし、出力ファイルパスに新しいファイルを作成します。

```
python3 file_manipulator.py reverse <入力ファイルパス> <出力ファイルパス>
```

### copy
指定した入力ファイルパスの中にあるファイルのコピーを作成し、出力ファイルパスにあるファイルを保存します。

```
python3 file_manipulator.py copy <入力ファイルパス> <出力ファイルパス>
```

### duplicate-contents
指定した入力ファイルパスにあるファイルの内容を読み込み、その内容を複製し、複製された内容を 指定した入力ファイルにN回複製します。

```
python3 file_manipulator.py duplicate-contents <入力ファイルパス> 繰り返し回数
```

### replace-string
指定した入力ファイルパスにあるファイルの内容から文字列needleを検索しneedleの全てをnewstringに置き換えます。

```
python3 file_manipulator.py replace-string <入力ファイルパス> needle newstring
```