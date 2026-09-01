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
