from engine.ai_engine import generate_context
from engine.decision_compiler import generate_page

context = generate_context()
generate_page(context)
print("Page published.")
