# Twitter Scrape Data
Twitter Scrap ini menggunakan Flask Framework dan lib snscrape

**SNScrape** :  <https://github.com/JustAnotherArchivist/snscrape/>

**Flask** :  <https://flask.palletsprojects.com/en/2.3.x//>

# Introduction


```javascript
    run python app.py
```

# API URL
```http
POST https://twit.ahmadsayadi.com/api/twit
```

## SNScrape Query
| Parameter | Description |
| :---  | :--- |
| `'its the elephant since:2020-06-01 until:2020-07-31'` | Berdasarkan Kata dengan Rentan Waktu |
| `'from:Ahmadsayadi_ since:2020-06-01 until:2020-07-31'` | Berdasarkan username dengan Rentan Waktu |



## Request
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `query` | `string` | **Required**. bisa menggunakan query di snscrape |
| `limit` | `number` | **Required**. limit data yang diinginkan |
| `jenis` | `string` | **Required**. `Cari Nama`/`Hashtag`/`String Kosong` |
| `lokasi` | `string` | **Required**. `latitude, longitude`/`String Kosong` |

**contoh** Lat lang: -7.25535576475254, 112.75319583481414, 10km (Surabaya)

## Example Request
ini adalah contoh request
```javascript
{
    "query":"Ahmadsayadi",
    "limit":100,
    "jenis":"",
    "lokasi":""
}
```



## Response Example
ini adalah response ketika disubmit
```javascript
{
    "data": [
        {
            "bookmarkCount": 0,
            "card": null,
            "cashtags": null,
            "conversationId": 1664260305101410312,
            "coordinates": null,
            "date": "Thu, 01 Jun 2023 13:19:11 GMT",
            "hashtags": null,
            "id": 1664260305101410312,
            "inReplyToTweetId": null,
            "inReplyToUser": null,
            "lang": "ca",
            "likeCount": 1,
            "links": null,
            "media": null,
            "mentionedUsers": null,
            "place": null,
            "quoteCount": 0,
            "quotedTweet": null,
            "rawContent": "Jika kau ingin menjadi orang yg kuat, maka belajarlah cara berperang melawan dirimu sendiri!",
            "renderedContent": "ا Jika kau ingin menjadi orang yg kuat, maka belajarlah cara berperang melawan dirimu sendiri!",
            "replyCount": 0,
            "retweetCount": 1,
            "retweetedTweet": null,
            "source": null,
            "sourceLabel": null,
            "sourceUrl": null,
            "url": "https://twitter.com/AhmadSayadi_/status/1664260305101410312",
            "user": {
                "created": "Sun, 12 Sep 2010 14:31:15 GMT",
                "descriptionLinks": null,
                "displayname": "Ahmad Sayadi",
                "favouritesCount": 688,
                "followersCount": 1431,
                "friendsCount": 1573,
                "id": 189891320,
                "label": null,
                "link": {},
                "listedCount": 6,
                "location": "Sudut Paling Sepi",
                "mediaCount": 585,
                "profileBannerUrl": "https://pbs.twimg.com/profile_banners/189891320/1654148139",
                "profileImageUrl": "https://pbs.twimg.com/profile_images/1649702037783986176/KStQzLXt_normal.jpg",
                "protected": null,
                "rawDescription": "Programmer || Blogger  || Daily Activity\n- Jadilah Orang Baik\n- Jangan Dibuat Nyaman Lalu Pergi Begitu Saja",
                "renderedDescription": "Programmer || Blogger  || Daily Activity\n- Jadilah Orang Baik\n- Jangan Dibuat Nyaman Lalu Pergi Begitu Saja",
                "statusesCount": 14267,
                "username": "AhmadSayadi_",
                "verified": false
            },
            "vibe": null,
            "viewCount": 41
        }
    ],
    "jenis": "",
    "msg": "success",
    "query": "bakso",
    "status_code": 1,
    "total_data": 5
}
```

`msg` adalah indikator pesan sebuah data sukses atau tidak

`status_code` untuk atribut kode sukses atau tidak.

`data` kumpulan data hasil scrape


## Status Code Response
Status Code Response

| Status Code | Description |
| :--- | :--- |
| 0 | `error` |
| 1 | `success` |

## Status Code
| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 400 | `BAD REQUEST` |

