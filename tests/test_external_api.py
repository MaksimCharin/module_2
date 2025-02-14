from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_to_rub_usd() -> None:
    with patch("requests.request") as mock_request:
        mock_response = mock_request.return_value
        mock_response.json.return_value = {"result": 75.0}
        result = convert_to_rub("USD")
        assert result == 75.0


def test_convert_to_rub_eur() -> None:
    with patch("requests.request") as mock_request:
        mock_response = mock_request.return_value
        mock_response.json.return_value = {"result": 85.0}
        result = convert_to_rub("EUR")
        assert result == 85.0
