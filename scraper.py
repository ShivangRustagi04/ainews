import requests
from bs4 import BeautifulSoup
import openai

# Set your OpenAI API key
openai.api_key =""

# Set the URL of the webpage you want to summarize
url = "https://www.prnewswire.com/news-releases/united-adds-new-corporate-partners-to-sustainable-flight-fund-that-now-exceeds-200-million-302061208.html"
req = requests.get(url)

if req.status_code == 200:
    soup = BeautifulSoup(req.content, "html.parser")
    paragraphs = soup.find_all('p')
    text_content = "\n".join([paragraph.get_text() for paragraph in paragraphs])

    # Use OpenAI GPT-3.5 Turbo to generate a summary
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text_content}
        ],
        max_tokens=150,
        temperature=0.5
    )

    summary = response['choices'][0]['message']['content']
    print("Generated Summary:")
    print(summary)


    video_generation_api_url = "https://studio.yepic.ai/dashboard"
    video_generation_api_key = ""
    
    video_generation_payload = {
        'input_text': summary,
        
    }
    
    video_generation_headers = {
        'Authorization': f'Bearer {video_generation_api_key}',
        'Content-Type': 'application/json'
    }
    
    video_generation_response = requests.post(video_generation_api_url, json=video_generation_payload, headers=video_generation_headers)
    

    print("Video Generation Response:", video_generation_response.text)

else:
    print(f"Failed to retrieve the page. Status code: {req.status_code}")


