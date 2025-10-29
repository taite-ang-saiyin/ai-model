from __future__ import annotations

import threading
from typing import Dict, Optional

from .models import Simulation


class SimulationRepository:
    """In-memory repository for simulations. Thread-safe for simple use cases."""

    def __init__(self):
        self._lock = threading.RLock()
        self._items: Dict[str, Simulation] = {}

    def add(self, simulation: Simulation) -> Simulation:
        with self._lock:
            self._items[simulation.id] = simulation
        return simulation

    def get(self, simulation_id: str) -> Optional[Simulation]:
        with self._lock:
            item = self._items.get(simulation_id)
            if item is None:
                return None
            # Return a copy to avoid accidental mutation outside the repository
            return Simulation.model_validate(item.model_dump())

    def update(self, simulation: Simulation) -> Simulation:
        with self._lock:
            if simulation.id not in self._items:
                raise KeyError(f"Simulation {simulation.id} not found.")
            self._items[simulation.id] = simulation
        return simulation

    def remove(self, simulation_id: str) -> None:
        with self._lock:
            self._items.pop(simulation_id, None)
