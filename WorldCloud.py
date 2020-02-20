from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://inbusiness.kz/ru"
html = urlopen(url).read()
soup = BeautifulSoup(html)
print(soup)

# удалить все элементы скрипта и стиля
for script in soup(["script", "style"]):
    script.extract()    # извлечение данных
print(soup)

text = soup.get_text()
print(text)

# разбить линии и убрать начальные и конечные пробелы в каждой строке
lines = (line.strip() for line in text.splitlines())
# разбить несколько заголовков в строке каждый
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# отбрасывать пустые строки 
text = '\n'.join(chunk for chunk in chunks if chunk)
print(text)

#скачать и распечатать стоп-слова для рус/каз языка
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('russian','kazakh'))
print(stop_words)

#токенизировать набор данных
words = word_tokenize(text)
print(words)

# удаляет знаки препинания и цифры
wordsFiltered = [word.lower() for word in words if word.isalpha()]
print(wordsFiltered)

# удалить стоп-слова из набора токенизированных данных
filtered_words = [word for word in wordsFiltered if word not in stopwords.words('russian','kazakh')]
print(filtered_words)


wc = WordCloud(max_words=1000, margin=10, background_color='white',
scale=3, relative_scaling = 0.5, width=500, height=400,
random_state=1).generate(' '.join(filtered_words))
plt.figure(figsize=(20,10))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
