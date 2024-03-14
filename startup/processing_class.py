from startup.my_log_class import LogHandler

l = LogHandler(__name__, log_file="log.txt", log_level=10, debug_mode=True, max_bytes=10000, backup_count=5, encoding="utf-8")
l.logger.debug("")