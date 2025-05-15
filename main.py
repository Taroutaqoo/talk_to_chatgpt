import speech_recognition as sr
from openai import OpenAI
import requests
import time
import configparser
import os
import winsound

print("▶ main.py 起動しました", flush=True)

# ini ファイル読み込み
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path, encoding="utf-8")
api_key = config["openai"]["api_key"]
client = OpenAI(api_key=api_key)

VOICEVOX_URL = "http://127.0.0.1:50021"
SPEAKER_ID = 0

system_prompt = """
あなたは「架空のキャラクター」です。以下のキャラクター設定、口調、関心を厳密に守ってふるまってください。

"""

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ マイク待ち…話してください", flush=True)
        audio = recognizer.listen(source)
        print("⚙️ 音声キャプチャ完了", flush=True)
    try:
        text = recognizer.recognize_google(audio, language="ja-JP")
        print("👤 あなた:", text, flush=True)
        return text
    except Exception as e:
        print("❓ 認識失敗:", e, flush=True)
        return None

def chat_with_airy(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    reply = response.choices[0].message.content
    print("🤖 あいり:", reply, flush=True)
    return reply

def speak_with_voicevox(text):
    try:
        r1 = requests.post(
            f"{VOICEVOX_URL}/audio_query",
            params={"text": text, "speaker": SPEAKER_ID}
        )
        r1.raise_for_status()
        query = r1.json()
        r2 = requests.post(
            f"{VOICEVOX_URL}/synthesis",
            params={"speaker": SPEAKER_ID},
            json=query
        )
        r2.raise_for_status()
        with open("output.wav", "wb") as f:
            f.write(r2.content)
        print("💾 output.wav 保存完了", flush=True)
        winsound.PlaySound("output.wav", winsound.SND_FILENAME)
        print("🔊 再生完了", flush=True)
    except Exception as e:
        import traceback
        print("‼️ 音声再生部で例外:", e, flush=True)
        traceback.print_exc()

# メインループ
while True:
    try:
        user_text = recognize_speech()
        if not user_text:
            print("↩︎ 再度マイク待ちに戻ります", flush=True)
            continue

        airy_reply = chat_with_airy(user_text)
        speak_with_voicevox(airy_reply)

        print("🔄 ループ終端。1秒スリープ後、次へ…", flush=True)
        time.sleep(1)
    except Exception as e:
        import traceback
        print("‼️ 重大な例外発生:", e, flush=True)
        traceback.print_exc()
        time.sleep(2)
