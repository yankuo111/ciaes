ps -ef | grep application.py | grep -v grep | awk '{print $2}' | xargs kill
CUDA_VISIBLE_DEVICES=-1 nohup python application.py >> ./cache/logs/server.log &
