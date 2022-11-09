import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:

        response = requests.get(url, {"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = []
    for url in selector.css("h2.entry-title > a::attr(href)"):
        news.append(url.get())

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url = selector.css("a.next::attr(href)").get()
    if url:
        return url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):

    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.head.find("link", {"rel": "canonical"})["href"]
    title = soup.body.h1.string
    writer = soup.body.find("span", {"class": "author"}).string
    timestamp = soup.body.find("li", {"class": "meta-date"}).string
    comments_count = soup.body.find_all("ol", {"class": "comment-list"})
    summary = soup.body.p.get_text()
    tags = []
    check_for_tags = soup.body.find("section", {"class": "post-tags"})
    category = soup.body.find("span", {"class": "label"}).string

    if check_for_tags:
        for tag in soup.select("section.post-tags > ul > li > a"):
            tags.append(tag.string)

    news = {
        "url": url,
        "title": title.replace("\xa0", "").rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": summary.replace("\xa0", "").rstrip(),
        "tags": tags,
        "category": category,
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
