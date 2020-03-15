# API
- 質問のタイプ
- 質問を取得する GET /v1/questions
- 回答を登録する POST /v1/answers

## 質問のタイプ
  - price 価格帯
  - hygiene 清潔度
  - volume ガッツリ度
  - waiting_time 提供時間
  - friendliness 店主の絡み度
  - distance_from_station 駅からの近さ
  - space 広さ
  - age_range 年齢層
  - stylishness オシャレ度

## 質問を取得する GET /v1/questions
- 質問を取得する。
- リクエスト
  - query parameter なし
  - body なし
- レスポンス
  - 質問を表す次の JSON が返却される。
  - 質問は4つ。度合は1～5の5つ。

```javascript
[
    {
        type: "<質問のタイプ>",
        description: "<質問の説明>",
        questions: [
            "<度合1の説明>", ..., "<度合5の説明>"
        ]
    }
    ...
]
```

## 回答を登録する POST /v1/answers
- 回答を登録して、オススメの店舗情報を取得する。
- リクエスト
  - query parameter なし
  - body
    - 回答を表す次の JSON を送信する。
    - 回答は5つ。度合は1～5の数字。

```javascript
[
    {
        type: "<質問のタイプ>",
        answerDegree: "<度合1～5>"
    }
    ...
]
```

- レスポンス
  - オススメ店舗情報を表す次の JSON が返却される。

```javascript
[
    {
        name: "<店舗の名前>",
        address: "<店舗の住所>",
        tel: "<店舗の電話番号>",
        status: "<店舗の営業状況>",
        open: "<店舗の開店時間>",
        close: "<店舗の閉店時間>",
        imageUrl: "<店舗の写真のURL>"
    }
    ...
]
```