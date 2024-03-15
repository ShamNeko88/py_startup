import os
from startup import config as con
"""
完成したプロジェクトフォルダを入れとくフォルダ作成
"""
os.makedirs(f"./{con.output}", exist_ok=True)