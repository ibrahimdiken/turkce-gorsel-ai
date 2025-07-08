import subprocess

def generate_detailed_prompt(user_input_tr):
    command = ["ollama", "run", "llama3"]
    prompt = (
        f"Aşağıdaki Türkçe cümleyi İngilizceye çevir ve görsel üretimi için uygun, detaylı ve betimleyici bir prompt haline getir:\n\n"
        f"{user_input_tr}"
    )
    result = subprocess.run(command, input=prompt, capture_output=True, text=True)
    return result.stdout.strip()
