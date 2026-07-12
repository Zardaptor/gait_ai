from .context_builder import build_context
from .prompt_builder import build_prompt
from .llm_interface import ask_llm

sensor = [
    20,
    18,
    22,
    19,
    15,
    -1.2,
    -5.8,
    7.6,
    -0.02,
    0.04,
    0.01
]

prediction = "Limp_Left"
confidence = 0.974

context = build_context(sensor, prediction, confidence)

prompt = build_prompt(context)

response = ask_llm(prompt)

print(response)