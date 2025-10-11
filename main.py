import os
from pathlib import Path
from openai import OpenAI


def tts(model: str, voice: str, text: str, output_file: str):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
    )

    output_path = Path(output_file)
    with open(output_path, "wb") as f:
        f.write(response.content)


def main():
    # https://platform.openai.com/docs/guides/text-to-speech
    # https://platform.openai.com/docs/api-reference/audio/createSpeech
    text = (
        "こんにちは。今日は素晴らしい天気ですね。"
        "音声合成技術を使って、自然な日本語の読み上げを試しています。"
        "この技術により、文章を音声に変換することができます。"
        "様々な用途に活用できる便利な機能です。"
    )
    tts("tts-1", "alloy", text, "output_alloy.mp3")
    tts("tts-1-hd", "alloy", text, "output_alloy_hd.mp3")


if __name__ == "__main__":
    main()
