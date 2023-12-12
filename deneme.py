import streamlit as st
import requests
import openai
from openai import OpenAI

api_key = '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'
openai.api_key = api_key
client = OpenAI(api_key=api_key)

# Sayfa başlığını ayarla
st.title("Çalışma Arkadaşım")

# Dersleri içeren bir slayt çubuğu oluştur
role_options = ["Fen bilgisi", "Hayat bilgisi", "Matematik", "Türkçe", "İngilizce"]
role = st.sidebar.selectbox("Ders", role_options)

# Kullanıcıdan bir mesaj al
message = st.text_input("Sorunuz")

# Chatbot'tan bir cevap al
response = client.chat.completions.create(
    model="gpt-4",
    temperature=0.2,
    max_tokens=1000,
    n=1,
    messages=[
        {"role": "system", "content": f"""Sen bir {role} öğretmenisin ve sadece ilkokul  {role} sorularına cevap vereceksin.
        Soruları 6-12 yaş arası bir çocuğun anlayabileceği şekilde cevaplar ver. 
        İngilizce sorulsa bile Türkçe cevap ver.
        Sorulan soruları analiz et. Branş dışı soruları tespit et. Branş dışı sorular da öğrenciyi ilgili branşa yönlendir.
        Kesinlikle dini ve siyasi konular hakkında ki sorulara cevap vermeyeceksin.
        Küfür ve hakaret dilini kullanmayacaksın."""},
        {"role": "user", "content": message}
    ]
)
response_text = response.choices[0].message.content

# Cevaplan yanıtı seslendir
st.speak(response_text)
