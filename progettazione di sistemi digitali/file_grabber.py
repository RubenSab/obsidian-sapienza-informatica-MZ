import os

def linked_files_from_file(file: str):
    
    with open(file, 'r') as f:

        text = f.read()
        import re
        matches = re.findall(r'\[([^|\]]*)\]|\[([^|\]]*)\|', text)
        links = [''.join(Match[0]+Match[1]) for Match in matches] 
        return [f'{filename}.md' for filename in links if f'{filename}.md' in os.listdir()]


file_texts = []
for file_name in linked_files_from_file('complementazione.md'):
    with open(file_name, 'r') as f:
        content = ''.join(f.read())
        file_texts.append(f'\n{file_name}:\n{content}')

files_content = ''.join(file_texts)
print(files_content)
