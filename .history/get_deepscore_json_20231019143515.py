import requests
import json

# 2. GraphQLのエンドポイントとヘッダーを設定
url = 'https://api.deepsource.io/graphql/'
headers = {
    'Authorization': 'Bearer dsp_bc2aa360f6cb40c8f9153868feb3ad9dbdaa'
}

# 3. クエリと変数を設定
query = '''
query($repoName: String!, $userName: String!, $vcsProvider: VCSProvider!) {
    repository(name: $repoName, login: $userName, vcsProvider: $vcsProvider) {
        analysisRuns(last: 1) {
            edges {
                node {
                status
                summary {
                    occurrenceDistributionByAnalyzer {
                    analyzerShortcode
                    introduced
                    }
                    occurrenceDistributionByCategory {
                    category
                    introduced
                    }
                }
                }
            }
        }
        enabledAnalyzers {
        edges {
            node {
            name
            issues(last:10) {
                edges {
                node {
                    title
                    analyzer {
                    name
                    }
                    autofixAvailable
                    category
                    severity
                    shortDescription
                }
                }
            }
            }
        }
        }
    }
}
'''
variables = {
    "repoName": "sample-apps",
    "userName": "katsuhisa",
    "vcsProvider": "GITHUB"
}

# 4. クエリを実行してレスポンスを取得
response = requests.post(url, headers=headers, json={'query': query, 'variables': variables})

# レスポンスが成功した場合
if response.status_code == 200:
    # 5. レスポンスをJSON形式で出力
    # レスポンスをJSON形式で取得
    data = response.json()
    # JSONファイルに保存
    with open('deepsource_response.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    
    print("Data has been saved to 'deepsource_response.json'")
else:
    print(f"Failed to execute query: {response.status_code}")
