"""
Validation utilities for quality gate compliance.
R5: Quality gate checks before rendering.
"""
from typing import List, Dict, Any


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_color_semantics(colors_used: Dict[str, str], allowed_colors: Dict[str, str]) -> bool:
    """
    R4: Validate that colors follow semantic rules.
    """
    for semantic, color in colors_used.items():
        if semantic in allowed_colors and color != allowed_colors[semantic]:
            raise ValidationError(
                f"Color semantic violation: {semantic} should be {allowed_colors[semantic]}, got {color}"
            )
    return True


def validate_scene_concept_count(concepts: List[str]) -> bool:
    """
    R2: Validate that scene explains only one concept.
    """
    if len(concepts) > 1:
        raise ValidationError(
            f"Scene concept violation: Scene explains {len(concepts)} concepts: {concepts}. "
            "Each scene must explain exactly one idea."
        )
    return True


def validate_animation_duration(duration: float, max_duration: float = 1.5) -> bool:
    """
    R8: Validate that animation duration is within limits.
    """
    if duration > max_duration:
        raise ValidationError(
            f"Duration violation: Animation duration {duration}s exceeds maximum {max_duration}s"
        )
    return True


def validate_no_magic_numbers(values: List[Any], allowed_constants: List[Any]) -> bool:
    """
    Validate that no magic numbers are used.
    """
    for value in values:
        if isinstance(value, (int, float)) and value not in allowed_constants:
            raise ValidationError(
                f"Magic number detected: {value}. Use named constants instead."
            )
    return True


def validate_relative_positioning(positioning_calls: List[str]) -> bool:
    """
    R6: Validate that no hard-coded coordinates are used.
    """
    absolute_patterns = ["move_to(", "set_x(", "set_y(", "set_z("]
    allowed_patterns = ["move_to(ORIGIN", "move_to(self.", "move_to(target."]
    
    for call in positioning_calls:
        for pattern in absolute_patterns:
            if pattern in call:
                is_allowed = any(allowed in call for allowed in allowed_patterns)
                if not is_allowed:
                    raise ValidationError(
                        f"Absolute positioning detected: {call}. Use relative positioning."
                    )
    return True


def validate_deterministic_array(array: List[int], expected: List[int]) -> bool:
    """
    R3: Validate that array is deterministic (predefined).
    """
    if array != expected:
        raise ValidationError(
            f"Non-deterministic array: Expected {expected}, got {array}"
        )
    return True


class QualityGate:
    """
    Quality gate checker for scenes.
    Must pass before rendering.
    """
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def check_all(
        self,
        colors_used: Dict[str, str] = None,
        concepts: List[str] = None,
        max_duration: float = None,
        positioning_calls: List[str] = None
    ) -> bool:
        """Run all validation checks."""
        try:
            if colors_used:
                from config.colors import (
                    UNPROCESSED, ACTIVE_COMPARISON, PIVOT,
                    CORRECTLY_PLACED, TEMPORARY_STORAGE
                )
                allowed = {
                    "unprocessed": UNPROCESSED,
                    "comparison": ACTIVE_COMPARISON,
                    "pivot": PIVOT,
                    "sorted": CORRECTLY_PLACED,
                    "temp": TEMPORARY_STORAGE
                }
                validate_color_semantics(colors_used, allowed)
            
            if concepts:
                validate_scene_concept_count(concepts)
            
            if max_duration:
                validate_animation_duration(max_duration)
            
            if positioning_calls:
                validate_relative_positioning(positioning_calls)
            
            return True
            
        except ValidationError as e:
            self.errors.append(str(e))
            return False
    
    def get_report(self) -> str:
        """Get validation report."""
        if not self.errors:
            return "✓ All quality checks passed"
        return "✗ Quality gate failed:\n" + "\n".join(f"  - {e}" for e in self.errors)
