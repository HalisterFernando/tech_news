import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    titles = []
    result = []
    for news in db.find_news():
        new_tuple = (news["title"], news["url"])
        titles.append(new_tuple)

    for tup in titles:
        if title.lower() in tup[0].lower():
            result.append(tup)

    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")

    news_by_date = db.find_news()
    result = []
    converted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
    for news in news_by_date:
        converted_news_date = datetime.strptime(
            news["timestamp"], "%d/%m/%Y"
        ).strftime("%d-%m-%Y")

        if converted_date == converted_news_date:
            new_tuple = (news["title"], news["url"])
            result.append(new_tuple)

    return result


# Requisito 8
def search_by_tag(tag):
    news_by_tag = db.find_news()
    result = []
    for news in news_by_tag:
        for item in news["tags"]:
            if tag.lower() == item.lower():
                new_tuple = (news["title"], news["url"])
                result.append(new_tuple)

    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
