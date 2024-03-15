import sys
from startup import config as con
from startup.my_log_class import LogHandler


######################################################################
# ログ管理系のインスタンス生成
######################################################################
try:
    if sys.argv[1] == "d":
        debug_mode:bool = True
    else:
        debug_mode:bool = False
except IndexError:
        debug_mode:bool = False
l = LogHandler(__name__, log_file="./log/log.txt", log_level=10, debug_mode=debug_mode, max_bytes=10000, backup_count=5, encoding="utf-8")
l.logger.debug("処理を開始しました。")


######################################################################
# エントリーポイント
######################################################################
def main():
    # 処理クラスインスタンス生成
    pc = Processing()

    # プロジェクト名を入力
    pr_name:str = pc.input_str("プロジェクト名を入力してください")

    # 設定ファイルから必要なファイルとフォルダを取得
    files:list = con.files
    l.logger.debug(f"ファイル類：{files}")
    dirs:list = con.dirs
    dirs.append(pr_name)
    l.logger.debug(f"フォルダ類：{dirs}")


######################################################################
# 処理系クラス
######################################################################
class Processing():
    def __init__(self) -> None:
        l.logger.debug("インスタンス生成")

    def input_str(self, txt):
        # コマンドラインから文字列入力
        l.logger.debug(f"コマンドラインから文字列入力：{txt}")
        return input(f"{txt} >>>>  ")


if __name__=="__main__":
    main()