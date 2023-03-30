import os
from pathlib import Path
import pandas as pd


diesel_sheet_name = 'DPCache_m3_2'
oilder_sheet_name = 'DPCache_m3'

path_sheet_from_root = Path(os.path.join('instance', 'vendas-combustiveis-m3.ods'))


def load(sheet_path: Path, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(sheet_path, sheet_name)

