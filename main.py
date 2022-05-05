# -*- coding: UTF-8 -*-
from config.settings import PORT
from src.lark_webhook import start as main

if __name__ == '__main__':
    main(PORT)

