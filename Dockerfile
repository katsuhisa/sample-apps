# ベースとなるイメージを指定
FROM python:3.9

# 作業ディレクトリを指定
WORKDIR /app

# ソースコードとrequirements.txtをコピー
COPY . /app

# Pythonの依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# シェルスクリプトに実行権限を付与
RUN chmod +x run_scripts.sh

# アプリケーションを実行
CMD ["./run_scripts.sh"]
