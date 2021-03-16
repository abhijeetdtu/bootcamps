import pathlib
import os

class dotdict(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(dotdict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(dotdict, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(dotdict, self).__delitem__(key)
        del self.__dict__[key]



config_dict = {
    "db_path" : "sqlite:///"+os.path.join(pathlib.Path(__file__).absolute().parent.parent , "bootcamp.db"),
    "csv_dump_path": os.path.join(pathlib.Path(__file__).absolute().parent , "dumps"),
    "registration" : dotdict({
        "sql_file": "create_registration_table.sql",
        "file_id" : "1zdInYO4atUXeTZhGwssc7EizJvZ1WzP0f1FkIs0p3X8",
        "sheet_id" : "Form Responses 1",
        "table_id" : "registration",
        "columns" : [
            "timestamp",
          "emailid",
          "first_name",
          "last_name",
          "banner_id",
          "program",
          "bootcamps",
          "statistics_knowledge",
          "python_knowledge",
          "r_knowledge",
          "is_processed"
        ]
    }),
    "registration_process" : dotdict({
        "sql_file" : "create_registration_process_view.sql"
    }),
    "grades" : dotdict({
        "sql_file": "create_grades_table.sql",
        "table_id" : "grades",
        "csv_dump_files" : dotdict({
            "intro_r" : "intro_r.csv",
            "intro_stats" : "intro_stats.csv",
            "intro_python" : "intro_python.csv"
        }),
        "columns" : [
            "full_name",
            "canvas_id",
            "user_id",
            "login_id",
            "section",
            "assignment",
            "score"
        ],
    }),
    "grades_tracker" : dotdict({
        "sql_file": "create_grades_tracker_view.sql"
    }),
    "bootcamps" : dotdict({
        "sql_file": "create_bootcamps_table.sql",
        "table_id"  : "bootcamps"
    }),
    "certificates":dotdict({
        "sql_file": "create_cert_table.sql"
    }),
    "cert_send" : dotdict({
        "sql_file": "fetch_cert_send.sql"
    }),
}

CONFIG = dotdict(config_dict)
