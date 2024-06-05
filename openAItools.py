import openai
import time
from config import openai_secret_key, openai_organization

openai.organization = openai_organization
openai.api_key = openai_secret_key

def create_chat_completion(user_question, max_tokens=150, temperature=0.7, retries=5, wait=60):
    for attempt in range(retries):
        try:
            response = openai.chat.completions.create(
                model = "gpt-3.5-turbo",
                # prompt = user_question,
                messages=[
                    {"role": "user", "content": user_question},
                ],
                max_tokens = max_tokens,
                temperature = temperature,
                # 在 OpenAI 的 GPT 模型中，temperature 是一個控制生成文本隨機性的參數，通常用於調整生成文本的多樣性。
                # 它影響了模型在生成下一個 token 時從可能選項中進行選擇的方式。
                # 這個參數的值通常在 0 到 1 之間，它控制了模型生成文本的 "溫度"。當溫度接近 0 時，模型會傾向於選擇概率最高的 token，這將產生比較確定性高的、重複性高的文本。
                # 當溫度接近無窮大時，模型將完全隨機地選擇 token，這將產生非常不可預測的、多樣性極高的文本。
                # 因此，調整 temperature 可以影響生成文本的多樣性和可預測性。在實際應用中，根據所需的結果，可以調整這個參數來平衡生成文本的多樣性和可控性。
                # 在上面的程式碼中，temperature=0 表示將溫度設置為 0，這意味著模型將傾向於生成最可能的 token，生成的文本可能會比較確定性高。
            )
            return response
        except openai.error.RateLimitError as e:
            if attempt < retries - 1:
                print(f"Rate limit exceeded. Retrying in {wait} seconds...")
                time.sleep(wait)
            else:
                raise e
