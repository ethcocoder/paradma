from .axiom import Axiom

class Bridge:
    """
    The Bridge: Synergy between the Mind (ParadoxLF) and Body (Paradma).
    Maps latent vectors to physical axioms.
    """
    @staticmethod
    def map_vector_to_axiom(vector: list, label: str = "identity"):
        """Converts a latent vector into a Paradma Axiom."""
        return Axiom(vector, label=label)

    @staticmethod
    def spooky_action(axiom_a: Axiom, axiom_b: Axiom):
        """
        Entangles two Axioms so that their values stay in sync.
        'Spooky Action at a Distance'.
        """
        if axiom_b not in axiom_a.entanglements:
            axiom_a.entanglements.append(axiom_b)
        if axiom_a not in axiom_b.entanglements:
            axiom_b.entanglements.append(axiom_a)
        
        # Sync current state (let A be dominant for sync)
        axiom_b.value = axiom_a.value
        return True
