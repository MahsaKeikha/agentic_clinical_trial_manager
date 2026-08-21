def evaluate(r:dict)->dict:
    required=["protocol_planner","site_coordinator","recruitment_tracker","data_quality","deviation_reviewer","reporting"]
    missing=[x for x in required if x not in r]
    return {"passed":not missing,"missing":missing}
