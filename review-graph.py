import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# JSONファイルを開いてデータを読み込む
with open('deepsource_response.json', 'r') as file:
    data = json.load(file)

# occurrenceDistributionByAnalyzerのデータを取得
analyzers_data = data['data']['repository']['analysisRuns']['edges'][0]['node']['summary']['occurrenceDistributionByAnalyzer']

# occurrenceDistributionByCategoryのデータを取得
categories_data = data['data']['repository']['analysisRuns']['edges'][0]['node']['summary']['occurrenceDistributionByCategory']

# データをpandas DataFrameに変換
analyzers_df = pd.DataFrame(analyzers_data)
categories_df = pd.DataFrame(categories_data)

# 指定したエラーカテゴリ
error_categories = ['ANTI_PATTERN', 'BUG_RISK', 'PERFORMANCE', 'SECURITY', 'COVERAGE', 'TYPECHECK', 'SECRETS', 'STYLE', 'DOCUMENTATION']

# 指定したカテゴリにデータがない場合は0を設定
for category in error_categories:
    if category not in categories_df['category'].values:
        categories_df = categories_df.append({'category': category, 'introduced': 0}, ignore_index=True)

# 追加：言語別の行数を読み込む
with open('language_lines.json', 'r') as file:
    language_lines = json.load(file)

# 追加：エラー率を計算するための関数
def calculate_error_rate(row):
    language = row['analyzerShortcode'].lower()  # 言語名を小文字に変換
    lines = language_lines.get(language, None)  # 言語別の行数を取得

    if lines is not None and lines > 0:
        return row['introduced'] / lines  # エラー率を計算
    else:
        return None  # 言語別の行数が取得できない場合はNoneを返す

# エラー率を計算
analyzers_df['error_rate'] = analyzers_df.apply(calculate_error_rate, axis=1)

# 追加：全ての言語のエラー数とコード行数を合計
total_errors = analyzers_df['introduced'].sum()
total_lines = sum(language_lines.values())

# 追加：全体のエラー率を計算
total_error_rate = total_errors / total_lines if total_lines > 0 else None

# 追加：全体のエラー率をデータフレームに追加
analyzers_df = analyzers_df.append({'analyzerShortcode': 'Total', 'error_rate': total_error_rate}, ignore_index=True)

# エラー率の棒グラフを作成
plt.figure(figsize=(10, 6))
sns.barplot(data=analyzers_df, x='analyzerShortcode', y='error_rate')
plt.title('Error Rate by Language')
plt.xlabel('Language')
plt.ylabel('Error Rate')
plt.savefig('error_rate_by_language.png')
