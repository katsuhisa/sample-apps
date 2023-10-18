#!/bin/bash

# DeepsourceのAPIを用いてJSONを生成
python get_deepscore_json.py

# GitHubの該当レポジトリのコードの行数をカウント
python rows_count.py

# JSONを元にエラー数をカウント
python error-category.py

# エラー数を元にエラー率を算出
python review-graph.py
