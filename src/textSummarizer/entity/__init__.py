
from dataclasses import dataclass
from pathlib import Path

#Define a decorator called 'dataclass'
# ENTITY - dATA iNGESTION
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# ENTITY - dATA Validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list