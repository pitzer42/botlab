clear
python -m unittest -v tests/*.py
: '
python -m unittest -v tests/test_interaction.py
python -m unittest -v tests/test_nlp.py
python -m unittest -v tests/test_storage.py
'
