import subprocess
from unittest import result


MODEL_NAME = "bartowski/microsoft_Phi-4-mini-instruct-GGUF"


SYSTEM_PROMPT = """
You are an AI Gait Intelligence Health Assistant.

You are NOT a doctor.

Never diagnose diseases.

Always respond ONLY in valid JSON.

The JSON format must be:

{
    "walking_summary":"",
    "balance_analysis":"",
    "risk_level":"",
    "rehabilitation_advice":[],
    "fall_prevention":[],
    "daily_exercises":[],
    "motivation":""
}
"""


def ask_llm(prompt):

    GENIEX_PATH = r"C:\Users\qcwor\AppData\Local\GenieX CLI\geniex.exe"

    command = [
        GENIEX_PATH,
        "infer",
        MODEL_NAME,
        "--system-prompt",
        SYSTEM_PROMPT,
        "--prompt",
        prompt,
        "--enable-json"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    output = result.stdout

    # Find the JSON block
    match = re.search(r"\{[\s\S]*\}", output)

    if match:
        json_text = match.group()

        try:
            return json.loads(json_text)
        except:
            return {
                "error": "Invalid JSON returned by Phi-4",
                "raw_output": json_text
            }

    return {
        "error": "No JSON found",
        "raw_output": output
    }