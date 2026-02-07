import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_debug_report_endpoint():
    payload = {
        "summary": "Test summary for API stability"
    }

    # Mock the LLM call
    with patch("src.api.main.generate_ml_debug_report") as mock_llm:
        mock_llm.return_value = "Mocked ML debug report"

        response = client.post("/debug-report", json=payload)

        assert response.status_code == 200
        assert "debug_report" in response.json()
        assert response.json()["debug_report"] == "Mocked ML debug report"