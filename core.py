from lit import Article

while True:
    article_name = input('Write here: ')
    if article_name == 'end':
        break
    article = Article(article_name)
    if article.is_apa():
        article.apa_parcing()
        if len(article.get_authors()) > 3:
            print(article.get_gost_more_3())
        elif len(article.get_authors()) == 3:
            print(article.get_gost_3())
        elif len(article.get_authors()) == 2:
            print(article.get_gost_2())
        elif len(article.get_authors()) == 1:
            print(article.get_gost_1())
    else:
        print('нужна сатья в формате APA')