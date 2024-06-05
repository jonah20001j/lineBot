# config.py
import os

from dotenv import load_dotenv

# 獲取當前目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
print('current_dir:' + current_dir)

# 構建上一層目錄的 .env 檔案路徑
dotenv_path = os.path.join(current_dir, '../', '.env')
print('dotenv_path:' + dotenv_path)

# 加載 .env 檔案
load_dotenv(dotenv_path)

# 獲取 line channel 金鑰
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
# 獲取 line control 金鑰
line_authtoken = os.getenv('LINE_AUTHTOKEN')
# 獲取 OpenAI 金鑰
openai_secret_key = os.getenv('OPENAI_SECRET_KEY')
# 獲取 OpenAI 組織
openai_organization = os.getenv('OPENAI_ORGANIZATION')
