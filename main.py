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
    with open(output_path, 'wb') as f:
        f.write(response.content)


def main():
    text = 'こんにちは。これはOpenAI Text-to-Speechのサンプルです。'
    tts('tts-1', 'alloy', text, 'output_alloy.mp3')
    tts('tts-1-hd', 'alloy', text, 'output_alloy_hd.mp3')


if __name__ == "__main__":
    main()
