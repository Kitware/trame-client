# export TRAME_CLIENT_TYPE=vue2
export TRAME_CLIENT_TYPE=vue3

rm -rf ./loading/
mkdir -p ./loading/loading_www
python -m trame.tools.www --client-type "$TRAME_CLIENT_TYPE" --output ./loading/loading_www
python -m wslink.launcher ./loading_launcher.json