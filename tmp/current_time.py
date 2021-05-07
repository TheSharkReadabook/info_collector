from datetime import datetime
from pytz import timezone

# 시스템 시간
def system_time():
    print(datetime.now())
    return datetime.now()
    
# KST
def KST_time():
    print(datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'))
    return datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
