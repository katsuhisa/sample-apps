import json
import pandas as pd

# JSONファイルを開いてデータを読み込む
with open('deepsource_response.json', 'r') as file:
    data = json.load(file)

# プログラミング言語別にカテゴリの出現回数をカウント
category_counts = {}
analyzers_data = data['data']['repository']['enabledAnalyzers']['edges']

for analyzer in analyzers_data:
    language = analyzer['node']['name']
    issues = analyzer['node']['issues']['edges']

    category_counts[language] = {}

    for issue in issues:
        category = issue['node']['category']
        category_counts[language][category] = category_counts[language].get(category, 0) + 1

# pandas DataFrameにデータを変換して表形式で出力
df = pd.DataFrame(category_counts).fillna(0).astype(int)
# 各列の合計を計算
df.loc['Column_Total'] = df.sum(numeric_only=True, axis=0)

# 各行の合計を計算
df['Row_Total'] = df.sum(numeric_only=True, axis=1)

print(df)