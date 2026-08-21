from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="planning"
    artifacts:dict=field(default_factory=dict)
