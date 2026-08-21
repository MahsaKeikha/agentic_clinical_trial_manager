class DataQualityAgent:
    name = "data_quality"
    def run(self, c: dict) -> dict: return {"data_quality": c.get("data_quality", {}), "reviewed": True}
