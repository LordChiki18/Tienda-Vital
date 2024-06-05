echo "BUILD START"
python3.11 --version
python3.11 -m ensurepip
python3.11 -m pip install -r requirements.txt
python3.11 manage.py collectstatic --noinput --clear
echo "BUILD END"