from dataclasses import dataclass,field
@dataclass
class TrialContext:
    protocol:dict
    sites:list=field(default_factory=list)
    recruitment:dict=field(default_factory=dict)
