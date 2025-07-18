import yaml

with open("spec/llm-spec.yaml") as f:
    spec = yaml.safe_load(f)

prompts = spec.get("llm_specification", {}).get("appendices", {}).get("prompt_templates", [])
for prompt in prompts:
    if "{{" not in prompt.get("template", ""):
        print(f"[WARN] Template '{prompt['name']}' may be missing variables.")
