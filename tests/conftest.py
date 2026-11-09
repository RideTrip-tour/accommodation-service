import os
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["DEBUG"] = "false"


from main import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def db():
    db = MagicMock()
    db.execute = AsyncMock()
    db.commit = AsyncMock()
    db.delete = AsyncMock()
    return db


@pytest.fixture
def session():
    session = MagicMock()
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    return session
