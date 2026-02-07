from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from src.llm.ml_debugger import generate_ml_debug_report

app = FastAPI(title="ML Debug Service")

class EvaluationSummary(BaseModel):
    summary: str

@app.post("/debug-report")
def debug_report(data: EvaluationSummary) -> Dict[str, str]:
    report = generate_ml_debug_report(data.summary)
    return {"debug_report": report}