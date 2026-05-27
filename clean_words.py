with open('oneword.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('oneword.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        line = line.replace('["', '').replace('"]', '').strip()
        if line:
            f.write(line + '\n')
