# %%
import os
from typing import Iterable
from pathlib import Path
import difflib
import itertools
from functools import cache

from dotenv import load_dotenv

local_env = Path('.env')
home_env = Path('~/.env').expanduser()
dotenv_file = local_env if local_env.exists() else home_env
if dotenv_file.exists():
  load_dotenv(dotenv_path=dotenv_file)

import hgvs.dataproviders.uta
import hgvs.normalizer
