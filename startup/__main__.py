import sys
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
l.logger.debug("処理を開始しました。")


def main():
    l.logger.debug("main関数の実行開始")




if __name__=="__main__":
    main()