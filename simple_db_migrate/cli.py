import argparse
import sys

class CLI(object):

    color = {
        "PINK": "",
        "BLUE": "",
        "CYAN": "",
        "GREEN": "",
        "YELLOW": "",
        "RED": "",
        "END": "",
    }

    @staticmethod
    def show_colors():
        CLI.color = {
            "PINK": "\033[35m",
            "BLUE": "\033[34m",
            "CYAN": "\033[36m",
            "GREEN": "\033[32m",
            "YELLOW": "\033[33m",
            "RED": "\033[31m",
            "END": "\033[0m",
        }

    @staticmethod
    def parse(args=None):
        parser = argparse.ArgumentParser()
        parser = CLI.options_to_parser(parser)
        parser.add_argument("-v", "--version",
                action="store_true",
                dest="simple_db_migrate_version",
                default=False,
                help="Displays simple-db-migrate's version and exit.")
        return parser.parse_args(args)

    @classmethod
    def options_to_parser(cls, parser):
        # type: (argparse.ArgumentParser) -> argparse.ArgumentParser
        parser.add_argument("-c", "--config",
                dest="config_file",
                default=None,
                help="Use a specific config file. If not provided, will search for 'simple-db-migrate.conf' in the current directory."),

        parser.add_argument("-l", "--log-level",
                dest="log_level",
                default=1,
                help="Log level: 0-no log; 1-migrations log; 2-statement execution log (default: %default)"),

        parser.add_argument("--log-dir",
                dest="log_dir",
                default=None,
                help="Directory to save the log files of execution"),

        parser.add_argument("--force-old-migrations", "--force-execute-old-migrations-versions",
                action="store_true",
                dest="force_execute_old_migrations_versions",
                default=False,
                help="Forces the use of the old migration files even if the destination version is the same as current destination "),

        parser.add_argument("--force-files", "--force-use-files-on-down",
                action="store_true",
                dest="force_use_files_on_down",
                default=False,
                help="Forces the use of the migration files instead of using the field sql_down stored on the version table in database downgrade operations "),

        parser.add_argument("-m", "--migration",
                dest="schema_version",
                default=None,
                help="Schema version to migrate to. If not provided will migrate to the last version available in the migrations directory."),

        parser.add_argument("-n", "--create", "--new",
                dest="new_migration",
                default=None,
                help="Create migration file with the given nickname. The nickname should contain only lowercase characters and underscore '_'. Example: 'create_table_xyz'."),

        parser.add_argument("-p", "--paused-mode",
                action="store_true",
                dest="paused_mode",
                default=False,
                help="Execute in 'paused' mode. In this mode you will need to press <enter> key in order to execute each SQL command, making it easier to see what is being executed and helping debug. When paused mode is enabled, log level is automatically set to [2]."),

        parser.add_argument("--color",
                action="store_true",
                dest="show_colors",
                default=False,
                help="Output with beautiful colors."),

        parser.add_argument("--drop", "--drop-database-first",
                action="store_true",
                dest="drop_db_first",
                default=False,
                help="Drop database before running migrations to create everything from scratch. Useful when the database schema is corrupted and the migration scripts are not working."),

        parser.add_argument("--show-sql",
                action="store_true",
                dest="show_sql",
                default=False,
                help="Show all SQL statements executed."),

        parser.add_argument("--show-sql-only",
                action="store_true",
                dest="show_sql_only",
                default=False,
                help="Show all SQL statements that would be executed but DON'T execute them in the database."),

        parser.add_argument("--label",
                dest="label_version",
                default=None,
                help="Give this label the migrations executed or execute a down to him."),

        parser.add_argument("--password",
                dest="password",
                default=None,
                help="Use this password to connect to database, to auto."),

        parser.add_argument("--env", "--environment",
                dest="environment",
                default="",
                help="Use this environment to get specific configurations."),

        parser.add_argument("--utc-timestamp",
                action="store_true",
                dest="utc_timestamp",
                default=False,
                help="Use utc datetime value on the name of migration when creating one."),

        parser.add_argument("--db-engine",
                dest="database_engine",
                default=None,
                help="Set each engine to use as sgdb (mysql, oracle, mssql). (default: 'mysql')"),

        parser.add_argument("--db-version-table",
                dest="database_version_table",
                default=None,
                help="Set the name of the table used to save migrations history. (default: '__db_version__')"),

        parser.add_argument("--db-user",
                dest="database_user",
                default=None,
                help="Set the username to connect to database."),

        parser.add_argument("--db-password",
                dest="database_password",
                default=None,
                help="Set the password to connect to database."),

        parser.add_argument("--db-host",
                dest="database_host",
                default=None,
                help="Set the host where the database is."),

        parser.add_argument("--db-port",
                dest="database_port",
                default=None,
                type="int",
                help="Set the port where the database is."),

        parser.add_argument("--db-name",
                dest="database_name",
                default=None,
                help="Set the name of the database."),

        parser.add_argument("--db-migrations-dir",
                dest="database_migrations_dir",
                default=None,
                help="List of directories where migrations are separated by a colon"),

        parser.add_argument("--info",
                dest="info_database",
                default=None,
                help="Show info of applied migrations (options: labels, last_label)"),

        return parser

    @classmethod
    def error_and_exit(cls, msg):
        cls.msg("[ERROR] %s\n" % msg, "RED")
        sys.exit(1)

    @classmethod
    def info_and_exit(cls, msg):
        cls.msg("%s\n" % msg, "BLUE")
        sys.exit(0)

    @classmethod
    def msg(cls, msg, color="CYAN"):
        print("{}{}{}".format(cls.color[color], msg, cls.color["END"]))
