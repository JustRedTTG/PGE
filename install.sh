cp pygameextra/version.py .
python3 -m build
pip install -e .
rm version.py
