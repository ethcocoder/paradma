import typing as t
from .axiom import Axiom
from .manifold import euclidean

class Universe:
    """
    A Universe is a collection of Axioms and Laws.
    It provides a high-level API for interacting with the substrate.
    """
    def __init__(self, name: str = "Default"):
        self.name = name
        self.axioms: t.List[Axiom] = []

    def add(self, value, **metadata):
        """Adds a new Axiom to the universe."""
        axiom = Axiom(value, **metadata)
        self.axioms.append(axiom)
        return axiom

    def apply(self, law_name: str, *args, **kwargs):
        """Applies a law to all Axioms in the universe or specific ones."""
        results = []
        for axiom in self.axioms:
            try:
                results.append(axiom.manifold.apply_law(law_name, axiom, *args, **kwargs))
            except AttributeError:
                continue
        return results

class NaturalLanguage:
    """
    A wrapper that allows users to define physics using 'Natural Laws'.
    Translates simple sentences into API calls.
    """
    def __init__(self, universe: Universe):
        self.universe = universe

    def execute(self, sentence: str):
        """
        Naive translation of sentences.
        Example: 'Apply Antigravity' -> universe.apply('antigravity')
        """
        words = sentence.lower().split()
        if "apply" in words:
            # Find the law name (e.g., words after 'apply')
            idx = words.index("apply")
            if idx + 1 < len(words):
                law_name = words[idx + 1]
                return self.universe.apply(law_name)
        
        if "add" in words:
            # Simple 'add 10' -> universe.add(10)
            try:
                val = float(words[words.index("add") + 1])
                return self.universe.add(val)
            except (ValueError, IndexError):
                pass
        
        return "Unknown command"
