"""
設定ファイル
"""

# 出力フォルダ
output:str = "result"

# 必要なファイル
files:list = ["README.md", ".gitignore"]

# 必要なフォルダ（ソースフォルダは別で追加）
dirs:list = ["docs", "tests"]