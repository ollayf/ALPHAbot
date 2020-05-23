# before running this, make sure to:
# 1. clone the repo by:
# $ git clone --branch <tag_name> https://github.com/ollayf/ALPHAbot.git
# 2. allow this script to be run by
# $ chmod +x ~/server_setup.sh
# 3. run the script by:
# $ ./server_setup.sh

python3.7 -m venv venv
cd venv
source bin/activate
cd ..
pip install -r requirements.txt

python3.7 main.py