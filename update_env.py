import os

def update_env_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return

    with open(filepath, 'r') as f:
        lines = f.readlines()

    has_base_url = False
    has_model = False

    new_lines = []
    for line in lines:
        if line.startswith('OPENAI_BASE_URL='):
            new_lines.append('OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/\n')
            has_base_url = True
        elif line.startswith('LLM_MODEL='):
            new_lines.append('LLM_MODEL=gemini-3.6-flash\n')
            has_model = True
        else:
            new_lines.append(line)

    if not has_base_url:
        new_lines.append('OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/\n')
    if not has_model:
        new_lines.append('LLM_MODEL=gemini-3.6-flash\n')
        
    # Rate limit variables
    has_delay = any(line.startswith('LLM_REQUEST_DELAY_SECONDS=') for line in lines)
    has_retries = any(line.startswith('LLM_MAX_RETRIES=') for line in lines)
    if not has_delay:
        new_lines.append('LLM_REQUEST_DELAY_SECONDS=3.0\n')
    if not has_retries:
        new_lines.append('LLM_MAX_RETRIES=5\n')

    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    print(f"Updated {filepath}")

update_env_file('.env')
update_env_file('.env.example')
