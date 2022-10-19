import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'chaustorage1014'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or 'HGlKAv/LG5nRani3h71HOm8QPXPt4ZcXG0b3rw7zZ8K1wdml1ILPI+nX9V9FUh9ipGwztWlt8rb++ASt/fGc3g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'chaucontainer'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'serverchaunow.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'chausqldb '
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'chauadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Admin@chou88'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "-xL8Q~BsEnT40y45l_QjRD.M8HgoOEo3uV0WBaeh"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault,CLIENT_SECRET or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv(
    #     "CLIENT_SECRET") or "-xL8Q~BsEnT40y45l_QjRD.M8HgoOEo3uV0WBaeh"
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/af869596-a9aa-4e35-b5f9-603fdc2b33ec"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "fbf74638-48cb-4848-8842-9efda4a45365"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session