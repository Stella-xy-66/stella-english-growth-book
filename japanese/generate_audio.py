import asyncio
from pathlib import Path

import edge_tts


VOICES = {
    "female": "ja-JP-NanamiNeural",
    "male": "ja-JP-KeitaNeural",
}

PHRASES = {
    "a-row": "あ。い。う。え。お。",
    "ka-row": "か。き。く。け。こ。",
    "ta-row": "た。ち。つ。て。と。",
    "hello": "こんにちは。",
    "excuse-me": "すみません。",
    "what-is-this": "これは何ですか？",
    "this-please": "これ、お願いします。",
    "thank-you": "ありがとうございます。",
    "this-that-and": "これ。それ。と。",
    "give-me-this": "これをください。",
    "this-and-that-please": "これとそれをお願いします。",
    "this-and-that-right": "これとそれですね。",
    "yes-please": "はい、お願いします。",
    "thanks-casual": "どうも。",
    "once-more-please": "もう一度お願いします。",
    "slowly-please": "ゆっくりお願いします。",
    "passport": "パスポートです。",
    "sightseeing": "観光です。",
    "days-stay-question": "何日間滞在しますか。",
    "days-stay-answer": "七日間です。",
    "hotel-reserved": "ホテルを予約しています。",
    "baggage-claim": "荷物受取所はどこですか。",
    "yes": "はい。",
    "dont-understand": "わかりません。",
    "japanese-little": "日本語があまり話せません。",
    "destination-station": "京都駅へ行きたいです。",
    "train-destination": "この電車は京都へ行きますか。",
    "transfer": "どこで乗り換えますか。",
    "exit-number": "何番出口ですか。",
    "check-in": "チェックインをお願いします。",
    "reservation-name": "スミスという名前で予約しています。",
    "luggage-storage": "荷物を預かってもらえますか。",
    "two-persons": "2人です。",
    "reservation": "予約しています。",
    "menu": "メニューをお願いします。",
    "recommendation": "おすすめは何ですか。",
    "water-please": "お水をお願いします。",
    "billing": "お会計お願いします。",
    "price": "いくらですか。",
    "card-accepted": "カードは使えますか。",
    "tax-free": "免税できますか。",
    "restroom-location": "トイレはどこですか。",
    "map-display": "地図で見せてもらえますか。",
    "help": "助けてください。",
    "good-morning": "おはようございます。",
    "good-evening": "こんばんは。",
    "goodbye-polite": "失礼します。",
}

KANA = """
あ い う え お か き く け こ さ し す せ そ た ち つ て と
な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん
が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ
きゃ きゅ きょ しゃ しゅ しょ ちゃ ちゅ ちょ にゃ にゅ にょ ひゃ ひゅ ひょ
みゃ みゅ みょ りゃ りゅ りょ ぎゃ ぎゅ ぎょ じゃ じゅ じょ びゃ びゅ びょ
ぴゃ ぴゅ ぴょ
""".split()


def codepoints(text: str) -> str:
    return "".join(f"{ord(char):x}" for char in text)


async def save(text: str, voice: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, voice).save(str(target))


async def main() -> None:
    audio_dir = Path(__file__).parent / "audio"
    for gender, voice in VOICES.items():
        for slug, text in PHRASES.items():
            await save(text, voice, audio_dir / f"phrase-{slug}-{gender}.mp3")
        for kana in KANA:
            await save(kana, voice, audio_dir / f"kana-{codepoints(kana)}-{gender}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
