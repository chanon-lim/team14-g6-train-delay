from config import wsgi
from train_delay.database_util import refresh_database
from test.testdata import main
from time import sleep

while True:
    sleep(60)
    main()

