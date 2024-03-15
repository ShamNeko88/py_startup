import sys
import tkinter.simpledialog as sd
from startup.my_log_class import LogHandler

# ログ管理系のインスタンス生成
try:
    if sys.argv[1] == "d":
        debug_mode:bool = True
    else:
        debug_mode:bool = False
except IndexError:
        debug_mode:bool = False

l = LogHandler(__name__, log_file="log.txt", log_level=10, debug_mode=debug_mode, max_bytes=10000, backup_count=5, encoding="utf-8")
l.logger.debug(f"処理クラスでログ管理インスタンスが生成されました。")

class Processing():
    def __init__(self) -> None:
        l.logger.debug("インスタンス生成")
    def input_str(self, txt):
        # プロジェクト名の入力
        return sd.SimpleDialog("入力", txt)