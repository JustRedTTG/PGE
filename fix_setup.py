import pygameextra

with open('setup.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if line.startswith('version'):
        lines[i] = f'version = "{pygameextra.__version__}"\n'
with open('setup.py', 'w') as f:
    f.writelines(lines)
