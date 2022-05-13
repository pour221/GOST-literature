import re


class Parcing:
    PATTERN_APA = r'(?:[A-Za-z-\']*, [A-Z]\.(?: ?[A-Z]\.)*[\. ,&]+)+\(\d{4}\)\. [A-Za-z 0-9\u2010\u2014\u2013\u2012\ufe6' \
                  r'3\u002d\-:,\.]+\. [\w \u2010\u2014\u2013\u2012\ufe63\u002d\-:,\(\)]+\.'

    def __init__(self, article_name):
        self.full_name = article_name

    def is_apa(self):
        return re.fullmatch(self.PATTERN_APA, self.full_name)

    def apa_parcing(self) -> None:
        '''
        takes the full name of the article, parses and returns a list of authors
        :return: list of authors
        '''
        pattern_authors_name = r'[A-Za-z-\']*, [A-Z]\.(?: ?[A-Z]\.)*'
        pattern_year = r'(?<![\u2010\u2014\u2013\u2012\ufe63\u002d])\d{4}(?![\u2010\u2014\u2013\u2012\ufe63\u002d])'
        pattern_pages = r'\d+(?:\–?\-?\d+)?.$'
        pattern_tom_number = r'\d+(?:\(\d+\))?, $'
        authors_list = re.findall(pattern_authors_name, self.full_name)
        for i in authors_list:
            self.full_name = self.full_name.replace(i, '')
        year = re.findall(pattern_year, self.full_name)
        self.full_name = self.full_name.replace(year[0], '')
        pages = re.findall(pattern_pages, self.full_name)
        self.full_name = self.full_name.replace(pages[0], '')
        tom_number = re.findall(pattern_tom_number, self.full_name)
        self.full_name = self.full_name.replace(tom_number[0], '')
        title, journal_name = self.full_name.strip(', .&()').split('.')
        if '(' in tom_number[0] and ')' in tom_number[0]:
            tom, number = tom_number[0].split('(')
            tom = tom.strip()
            number = number.strip(', )')
            self.__journal_number = number
            self.__journal_tom = tom
        elif '(' in tom_number[0] or ')' in tom_number[0]:
            print('!ОШИБКА в парсинге тома и номера!')
        else:
            self.__journal_number = tom_number[0].strip(' ,')
            self.__journal_tom = False
        for i in authors_list:
            authors_list[authors_list.index(i)] = i.replace('. ', '.')
        self.__authors = authors_list
        self.__year = year[0]
        self.__title = title
        self.__journal = journal_name.strip()
        self.__pages = pages[0].strip('.')

    def get_authors(self):
        return self.__authors

    def get_year_of_article(self):
        return self.__year

    def get_article_title(self):
        return self.__title

    def get_journal(self):
        return self.__journal

    def get_journal_number(self):
        return self.__journal_number

    def get_journal_tom(self):
        return self.__journal_tom

    def get_journal_pages(self):
        return self.__pages



if __name__ == '__main__':
    what = input('Write here: ')
    article = Parcing(what)
    print(what)
    print(article.is_apa())

