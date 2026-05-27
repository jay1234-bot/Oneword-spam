import json

with open('oneword.txt', 'r', encoding='utf-8') as f:
    text = f.read().strip()
    if not text.startswith('['):
        text = '[' + text + ']'
        
    try:
        words = json.loads(text)
    except Exception as e:
        print("Fallback parse")
        words = [w.strip(' "\'') for w in text.split(',')]

with open('oneword.txt', 'w', encoding='utf-8') as f:
    for w in words:
        if w.strip():
            f.write(w.strip() + ',\n')
