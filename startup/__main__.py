import sys
import os
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
l.logger.debug("################# 処理を開始しました #############################")


######################################################################
# エントリーポイント
######################################################################
def main():
    # 処理クラスインスタンス生成
    try:
        pc = Processing()
        l.logger.debug("処理クラスインスタンス生成")
    except:
        l.logger.error("処理クラスのインスタンスを生成できませんでした")
    try:
        # プロジェクト名を入力
        pr_name:str = pc.input_str("プロジェクト名を入力してください")
        l.logger.debug(f"プロジェクト名を取得しました：{pr_name}")
    except:
        l.logger.error("プロジェクト名を取得できませんでした")

    # 設定ファイルから必要なファイルとフォルダを取得
    try:
        files:list = con.files
        dirs:list = con.dirs
        dirs.append(pr_name)
        l.logger.debug("設定ファイルから必要なファイルとフォルダを取得しました")
    except:
        l.logger.error("設定ファイルから必要なファイル名とフォルダ名の取得ができませんでした")
    # フォルダの作成、ファイル作成
    try:
        pc.maker(pr_name, dirs, files)
        l.logger.debug("フォルダとファイル作成")
    except:
        l.logger.error("フォルダとファイルを作成できませんでした")



######################################################################
# 処理系クラス
######################################################################
class Processing():
    # コマンドラインから文字列入力
    def input_str(self, txt):
        return input(f"{txt} >>>>  ")
    
    # フォルダ作成、ファイル作成
    def maker(self, pr_name:str, dirs:list, files:list):
        for i in range(len(dirs)):
            os.makedirs(f"./{con.output}/{pr_name}/{dirs[i]}", exist_ok=True)
        
        for x in range(len(files)):
            with open(f"./{con.output}/{pr_name}/{files[x]}", "w") as f:
                f.write("")

    


if __name__=="__main__":
    main()