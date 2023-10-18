import requests
import os
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

# 各パスに対してリクエストを送り、情報を取得
for path in paths:
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.json()
        print(json.dumps(content, indent=4))  # 取得したJSONを整形して出力
    else:
        print(f"Failed to retrieve the content of {path}")
        print(response.content)  # エラーメッセージを出力

