class State:
    ...


class StateMachine:
    def __init__(self, transitions: dict[State, State]) -> None:
        """
        s0 => s1 # start
        s1 => s2
        s2 => s3 # end
        """
        self.transitions = transitions

    def evolve(self) -> None
        self.current_state = transitions[self.current_state]

    

class FiniteStateMachine(StateMachine)
    def __init__(self) -> 
