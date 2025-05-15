# talk_to_chatgpt
ChatGPTと音声で会話する
ChatGPT会話スクリプト

このスクリプトは、音声認識 + ChatGPT + VOICEVOX音声合成で、
お好きなボイスでChatGPTとと音声会話できるデスクトップアプリです。


動作確認環境

Windows 10/11
Python 3.13.3
マイクが使用できる環境
VOICEVOXエンジン

---

免責事項

* 本ソフトウェアの利用により発生した損害について、
  開発者は一切の責任を負いません。
* 本ソフトウェアは個人利用を想定しています。
* OpenAI API利用は各自の責任で管理・課金設定してください。
* VOICEVOXの利用規約を遵守してください。

---

導入手順

1. Pythonのインストール

[公式Pythonダウンロードページ](https://www.python.org/downloads/windows/)
からインストールしてください。

インストール時に「Add Python to PATH」にチェックを入れてください。

---

2. 必要なライブラリのインストール

コマンドプロンプト（またはPowerShell）で、
main.py と同じフォルダに移動して以下を実行します：

pip install openai requests SpeechRecognition pyaudio

---

3. VOICEVOXエンジンのセットアップ

[VOICEVOX公式ページ](https://voicevox.hiroshiba.jp/) から
 Windows版エンジンをダウンロードしてインストールしてください。
 VOICEVOXエンジンを起動し、デフォルトの http://127.0.0.1:50021 で待機させてください。

---

4. OpenAI APIキーの取得・設定

 [OpenAI公式ページ](https://platform.openai.com/account/api-keys) にアクセスし、APIキーを取得します（`sk-...` で始まる文字列）。
 プロジェクトのフォルダに ”config.ini” を作り、以下の内容を書いて保存します。

[openai]
api_key = sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX←あなたのAPIキー


5. プログラムの実行

コマンドプロンプトで次のコマンドを実行します：

python main.py

---

ライセンス

* 本ソフトウェアの利用は自己責任でお願いします。
* 商用利用・二次配布はご遠慮ください。


謝辞

* [VOICEVOX](https://voicevox.hiroshiba.jp/)
* [OpenAI GPT API](https://platform.openai.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
