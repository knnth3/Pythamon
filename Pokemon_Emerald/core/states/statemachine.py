from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self):
        self.running = False
        self.updateInBackground = False
    
    def enable(self):
        self.onEnable()
        self.running = True

    def disable(self):
        self.onDisable()
        self.running = False

    def setStateMachine(self, statemachine):
        self.statemachine = statemachine

    def deactivateSelf(self):
        if self.statemachine == None:
            return

        if self.statemachine.currentState == self:
            self.statemachine.deactivateState()

    def activateNewState(self, newState, overrideCurrent: bool = False):
        if self.statemachine == None:
            return
        
        self.statemachine.activateState(newState, overrideCurrent)

    @abstractmethod
    def onEnable(self):
        pass

    @abstractmethod
    def onDisable(self):
        pass

    @abstractmethod
    def onUpdate(self, deltaTime, events):
        pass

class StateMachine():
    def __init__(self, init_state: GameState):
        self.currentState = None
        self.activateState(init_state)

    def update(self, deltaTime, events: list[any]):
        if self.background_state and self.background_state.running and self.background_state.updateInBackground:
            if self.currentState.onUpdate(deltaTime, events) == -1:
                return -1

        if (self.currentState and self.currentState.running):
            if self.currentState.onUpdate(deltaTime, events) == -1:
                return -1

        return 0
    
    def activateState(self, state: GameState, overrideCurrent: bool = False):
        if (overrideCurrent == False):
            self.background_state = self.currentState
        elif self.currentState != None:
            self.currentState.setStateMachine(None)
            self.currentState.disable()

        self.currentState = state
        if self.currentState != None:
            self.currentState.setStateMachine(self)
            self.currentState.enable()

    def deactivateState(self):
        if self.currentState != None:
            self.currentState.setStateMachine(None)
            self.currentState.disable()
            if self.background_state != None:
                self.currentState = self.background_state
                self.background_state = None


