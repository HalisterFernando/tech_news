import tech_news.database as db


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
