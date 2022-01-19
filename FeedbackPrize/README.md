# Competitions
- [Feedback Prize - Evaluating Student Writing](https://www.kaggle.com/c/feedback-prize-2021/overview/description)
- 締め切りは3/16

## コンペの背景
- アメリカ人学生の文章力を鍛えたい。
- エッセイを提出してもらい、それを人が添削してフィードバックを行なっている。
- それを自動化するモデルを作成したい。

## 分析内容
- エッセイに対して人間がつける注釈を予測する。
- 注釈は以下
    - `Lead`: 統計、引用、説明、または読者の注意を引き、論文に向けるその他のデバイスで始まる紹介
    - `Position`: 主な質問に対する意見または結論
    - `Claim`: 立場を支持する主張
    - `Counterclaim`: 別の主張に反論する、またはその立場に反対の理由を与える主張
    - `Rebuttal`: 反訴に反論する主張
    - `Evidence`: 主張、反訴、または反論を裏付けるアイデアまたは例。
    - `Concluding Stgatement`: 結論

## データ
### 概要
- 大きく2つのデータが与えられている。
    - train/*.txt
        - 15595件のテキストファイル
        - (英文の?)エッセイ
    - trian.csv
        - エッセイのアノテーションデータ
        - カラム名は以下の表の通り

| id | discource_id | discource_start | discource_end | discource_text | discource_type | discource_type_num | predictionstring |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| エッセイID | 要素のID | エッセイの応答で談話要素が始まる文字の位置 | 談話要素がエッセイ応答で終了する文字位置 | 談話要素のテキスト | 談話要素の分類 | 談話要素の列挙されたクラスラベル | 予測に必要なトレーニングサンプルの単語インデックス |



### 中身

423A1CA112E2.txt

Phones

<span style="color: red; ">Modern humans today are always on their phone. They are always on their phone more than 5 hours a day no stop .All they do is text back and forward and just have group Chats on social media. They even do it while driving.</span> They are some really bad consequences when stuff happens when it comes to a phone. Some certain areas in the United States ban phones from class rooms just because of it.

When people have phones, they know about certain apps that they have .Apps like Facebook Twitter Instagram and Snapchat. So like if a friend moves away and you want to be in contact you can still be in contact by posting videos or text messages. People always have different ways how to communicate with a phone. Phones have changed due to our generation.

Driving is one of the way how to get around. People always be on their phones while doing it. Which can cause serious Problems. That's why there's a thing that's called no texting while driving. That's a really important thing to remember. Some people still do it because they think It's stupid. No matter what they do they still have to obey it because that's the only way how did he save.

Sometimes on the news there is either an accident or a suicide. It might involve someone not looking where they're going or tweet that someone sent. It either injury or death. If a mysterious number says I'm going to kill you and they know where you live but you don't know the person's contact

,It makes you puzzled and make you start to freak out. Which can end up really badly.

Phones are fine to use and it's also the best way to come over help. If you go through a problem and you can't find help you ,always have a phone there with you. Even though phones are used almost every day as long as you're safe it would come into use if you get into trouble. Make sure you do not be like this phone while you're in the middle of driving. The news always updated when people do something stupid around that involves their phones. The safest way is the best way to stay safe. 




| id | discource_id | discource_start | discource_end | discource_text | discource_type | discource_type_num | predictionstring |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|423A1CA112E2 | 1622627660524 | 8 | 229 | Modern humans today are always on their phone....	| Lead | Lead 1 | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1... |
| 423A1CA112E2 | 1622627653021 | 230 | 312 | They are some really bad consequences when stu... | Position | Position 1 | 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 |
| 423A1CA112E2 | 1622627671020 | 313 | 401 | Some certain areas in the United States ban ph... | Evidence | Evidence 1 | 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 |
| 423A1CA112E2 | 1622627696365 | 402 | 758 | When people have phones, they know about certa...	 | Evidence | Evidence 2 | 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 9... |
| 423A1CA112E2 | 1622627759780 | 759 | 886 | Driving is one of the way how to get around. P... | Claim | Claim 1 | 139 140 141 142 143 144 145 146 147 148 149 15... |
| 423A1CA112E2 | 1622627780655 | 887 | 1150 | That's why there's a thing that's called no te... | Evidence | Evidence 3	| 163 164 165 166 167 168 169 170 171 172 173 17... |
| 423A1CA112E2 | 1622627811787 | 1151 | 1533 | Sometimes on the news there is either an accid... | Evidence | Evidence 4 | 211 212 213 214 215 216 217 218 219 220 221 22... |
| 423A1CA112E2 |1622627585180 | 1534 | 1602	| Phones are fine to use and it's also the best ... | Claim	| Claim 2 | 282 283 284 285 286 287 288 289 290 291 292 29... |
| 423A1CA112E2 | 1622627895668 | 1603 | 1890 | If you go through a problem and you can't find... | Evidence	| Evidence 5 | 297 298 299 300 301 302 303 304 305 306 307 30... |
| 423A1CA112E2 | 1622627628524 | 1891 | 2027 | The news always updated when people do somethi... | Concluding Statement	| Concluding Statement 1 | 355 356 357 358 359 360 361 362 363 364 365 36... |


### その他注意事項
- エッセイの一部には注釈がつけられていない。
- 空白・改行なども一文字に数えられている。
- ここでの正解は、談話タイプと予測文字列の組み合わせ
    - 正しい談話タイプが予測されているが、単語の長さが違う場合は、部分的に一致する可能性がある。


## 提出方法
- Code Competition
    - notebookでの提出を行う
    - 出力カラムはid,class,predictionstring

## 評価方法
- [こちら](https://www.kaggle.com/c/feedback-prize-2021/overview/evaluation)を参照

## EDA
- [EDA](https://www.kaggle.com/nakaotomohiro/feedback-prize-eda-by-nakao)
