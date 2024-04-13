"""The update objective tool. Copyright (C) 2024 SynaLinks. License: GPL-3.0"""

import copy
import dspy
from .base import BaseTool
from typing import Optional, Callable
from ..types.state import AgentState

class ClearTraceTool(BaseTool):

    def __init__(
            self,
            agent_state: AgentState,
        ):
        super().__init__(name = "ClearTrace")
        self.agent_state = agent_state
        
    def forward(
            self,
            context: str,
            objective: str,
            purpose: str,
            prompt: str,
            disable_inference: bool = False,
        ) -> dspy.Prediction:
        """Method to perform DSPy forward prediction"""
        self.agent_state.program_trace = []
        return None

    def __deepcopy__(self, memo):
        cpy = (type)(self)(
            agent_state = self.agent_state,
        )
        return cpy
