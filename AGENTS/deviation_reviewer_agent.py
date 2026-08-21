class DeviationReviewerAgent:
    name = "deviation_reviewer"
    def run(self, c: dict) -> dict: return {"deviations": c.get("deviations", []), "human_review": True}
