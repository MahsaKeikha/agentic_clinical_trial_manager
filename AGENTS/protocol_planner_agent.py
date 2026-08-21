class ProtocolPlannerAgent:
    name = "protocol_planner"
    def run(self, c: dict) -> dict: return {"protocol": c.get("protocol", {}), "planned": True}
