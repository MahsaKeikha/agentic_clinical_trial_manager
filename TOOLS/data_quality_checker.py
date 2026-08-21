def review(data: dict) -> dict: return {"reviewed": True, "missing": [k for k,v in data.items() if v is None]}
