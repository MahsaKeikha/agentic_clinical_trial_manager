class SiteCoordinatorAgent:
    name = "site_coordinator"
    def run(self, c: dict) -> dict: return {"sites": c.get("sites", []), "coordinated": True}
