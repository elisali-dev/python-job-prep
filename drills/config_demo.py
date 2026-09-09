import os 
from dotenv import load_dotenv
from pathlib import Path

# load_dotenv() 直接从当前运行文件夹根目录(依赖你从哪个 terminal directory 启动程序)下找.env 

env_path = Path(__file__).parent/".env"
load_dotenv(env_path)
 # load_dotenv() 不是返回一个 config dict 给你，而是把 .env 里的值加载进当前 Python process 的 environment 里。
 # 默认不会覆盖已经存在的 environment variable。所以如果 shell 里有, .env 也有, 还是取 shell environment 里面的值



passing_score = int(
    os.getenv("PASSING_SCORE")
)

print(passing_score)
print(type(passing_score))

app_env = os.getenv("APP_ENV")