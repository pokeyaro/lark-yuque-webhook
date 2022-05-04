# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from settings import PORT
from src.lark_webhook import start as main


if __name__ == '__main__':
    main(PORT)

