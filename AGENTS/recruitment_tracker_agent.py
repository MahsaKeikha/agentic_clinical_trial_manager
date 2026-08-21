class RecruitmentTrackerAgent:
    name = "recruitment_tracker"
    def run(self, c: dict) -> dict: return {"recruitment": c.get("recruitment", {}), "tracked": True}
