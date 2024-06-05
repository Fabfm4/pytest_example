from unittest.mock import patch
from src.execute_user import get_user_from_py


def test_user_one():
    with patch("src.execute_user.get_user") as mock_get_user:
        mock_get_user.return_value = "user 2"
        result = get_user_from_py()
        assert result == "user 2"
        assert 1 == 2
