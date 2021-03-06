class AppLogger:
    """ the logger to log for the app """

    def __init__(self, app_config, name):
        self.app_config = app_config
        self.file_name = name

    def write_line(self, obj):
        # app_config has the debugging option
        # when not debugging, don't log
        if self.app_config["run_mode"] != "debug":
            return
        # log the message to the log file
        print("%s" % obj)
        f = open(self.file_name, "a")
        f.write("%s" % obj)
        f.write("\n")
        f.close()
