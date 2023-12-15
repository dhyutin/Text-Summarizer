# ENTITY - dATA iNGESTION
from dataclasses import dataclass
from pathlib import Path

#Define a decorator called 'dataclass'
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path