import requests
import json

# GitHubの認証トークンを環境変数から取得
token = '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'

# 対象のGitHubリポジトリ
owner = 'LLM-HACKATHON-Team5'
repo = 'sample-apps'

# 対象のパスのリスト
paths = ['blog-apps', 'calcurator-apps', 'counter-apps']

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

files = []

# 各パスに対してリクエストを送り、情報を取得
for path in paths:
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.json()
        for item in content:
            if item['type'] == 'file':  # ディレクトリを除外
                files.append({
                    'name': item['name'],
                    'download_url': item['download_url']
                })
    else:
        print(f"Failed to retrieve the content of {path}")
        print(response.content.decode())  # エラーメッセージを出力

# ファイルの行数をカウント
language_lines = {}

for file in files:
    response = requests.get(file['download_url'])
    if response.status_code == 200:
        lines = response.text.split('\n')
        extension = file['name'].split('.')[-1]

        # 各プログラミング言語の拡張子と言語名のマッピング
        language_mapping = {
            'py': 'python',
            'js': 'javascript',
            'html': 'html',
            'php': 'php',
            'rb': 'ruby',
            'rs': 'rust',
            'c': 'c'
            # 必要に応じて他の言語も追加できます
        }
        
        language = language_mapping.get(extension, extension)  # 拡張子に対応する言語名を取得、対応がない場合は拡張子をそのまま使用
        language_lines[language] = language_lines.get(language, 0) + len(lines)
    else:
        print(f"Failed to retrieve the content of {file['name']}")

# 各言語の行数をJSON形式で出力
print(json.dumps(language_lines, indent=4))

# 最後の部分をこのように変更
with open('language_lines.json', 'w') as file:
    json.dump(language_lines, file, indent=4)