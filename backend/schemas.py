from typing import List, Optional

from pydantic import BaseModel, Field

from .models import (
    AgentCustomization,
    AgentProfile,
    AgentRelationshipSeed,
    Simulation,
)


class CreateSimulationRequest(BaseModel):
    scenario: str = Field(..., min_length=1)
    custom_agents: List[AgentCustomization] = Field(default_factory=list, max_length=5)
    agent_profiles: List[AgentProfile] = Field(default_factory=list, max_length=5)
    relationships: List[AgentRelationshipSeed] = Field(
        default_factory=list, max_length=20
    )


class SimulationResponse(BaseModel):
    simulation: Simulation


class AdvanceSimulationRequest(BaseModel):
    steps: int = Field(1, ge=1, le=50)


class FateWeaverRequest(BaseModel):
    prompt: Optional[str] = Field(None, description="Optional user-crafted twist.")
