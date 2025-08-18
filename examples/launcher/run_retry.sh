export TRAME_CLIENT_TYPE=vue3

rm -rf ./www/
python -m trame.tools.www --client-type "$TRAME_CLIENT_TYPE" --output ./www
python -m wslink.launcher ./retry_launcher.json
