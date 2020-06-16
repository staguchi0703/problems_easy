# AtCoder ABCxxx

## 目的

* ABCでテストケースを使う準備をする
* 参加後に解答を整理すことで、今後の参考資料とする
  

## 問題解説

### A

* パス

### B

* パス

### C

#### 方針

#### 実装

```python:C.py

```

### D

#### 方針

#### 実装

```python:D.py

```

### E/F

* できる見込みなし！

## このリポジトリの使い方

### 参加前とコンテスト中
1. github上で`templete`をクローンしたリポジトリを作成し、参加コンテストの名前を付ける。
   * レポジトリを新規作成する画面に遷移した際に、他のリポジトリを取り込むリンクがあるので、そこから作成すると早い。 
2. ローカルに複製する。　`git clone {repo}`
   * 複製するとローカルリポジトリのディレクトリに自動で飛ぶ。
   * そこで`code .`すれば、そのまま今回のコンテストに必要なディレクトリだけを持ったworkingspaceが立ち上がる。
3. テストケースの値を各問題フォルダの`input.txt`にペースト
4. 回答をa_main.pyに記入
5. 実行して動作確認する。terminalからのpython実行をキーバインドするのが〇
6. `output.txt`に期待する出力をいれて、`resolve.py`に提出するコードを入力しておけば、`test_resolve_form_input_files.py`でunittestが実行できる。
7. chrome pluginのAtcoder_unittestの内容を`test_pasted_from_page.py`にペーストすれば、全ての出力例の確認ができる。

### 参加後
* 苦戦した問題と、コンテスト後にACした問題の解説を書く

### その他
* 画面スペースに余裕があれば、`resolve.py`と`test_pasted_from_page.py`と`terminal`の3画面で作業した方が速いかも。
* 途中の確認をprintでバグするなら`a_main.py`でいじる方が分かりやすい。
