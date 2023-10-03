# PEP 8 – Python コードのスタイル ガイド

- [PEP 8 – Python コードのスタイル ガイド](https://peps.python.org/pep-0008/)

# ルール

- インデント レベルごとに 4 つのスペース

- すべての行を最大 79 文字に制限

- 関数とクラスの定義は 2 つの空白行

- クラス内のメソッド定義は 1 つの空白行

- コードは常に UTF-8 を使用する必要があり、エンコード宣言不要

- インポートは次の順序でグループ化
    - 標準ライブラリ
    - 関連するサードパーティ
    - ローカル アプリケーション/ライブラリ固有
    - インポートの各グループの間に空行

- クラス名には通常、CapWords 規則を使用

- 関数・変数名は小文字で必要に応じて単語をアンダースコアで区切る

- インスタンスメソッドの最初の引数には self を常に使用

- クラスメソッドの最初の引数には cls を常に使用

- 定数はすべて大文字で必要に応じて単語をアンダースコアで区切る