echo [$(date)]: "START"

echo [$(date)]: "Creating env with python 3.8 version"

conda create --prefi ./env pythpn =3.8-y

echo [$(date)]: "activating the environment"
conda activate ./env
echo [$(date)]: "installing the requirements"
pip install -r requirements.txt
echo [$(date)]: "END"
