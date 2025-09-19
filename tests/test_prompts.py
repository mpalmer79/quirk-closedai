from src.utils.prompt_loader import Prompts


def test_compose_includes_all():
p = Prompts()
base = p.compose()
assert "Mission:" in base and "Core behavior" in base
