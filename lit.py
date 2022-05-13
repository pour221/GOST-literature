from parcing import Parcing


class Article(Parcing):
    def get_gost_more_3(self) -> str:
        '''

        :return:
        '''
        main_author = [author.strip() for author in self.get_authors()[0].split(',')]
        if self.get_journal_tom():
            return f'{self.get_article_title()} / {main_author[1]} {main_author[0]} [et al.] // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}'
        else:
            return f'{self.get_article_title()} / {main_author[1]} {main_author[0]} [et al.] // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}'

    def get_gost_3(self) -> str:
        '''

        :return:
        '''
        main_author = [author.strip() for author in self.get_authors()[0].split(',')]
        seconde_author = [author.strip() for author in self.get_authors()[1].split(',')]
        third_author = [author.strip() for author in self.get_authors()[2].split(',')]
        if self.get_journal_tom():
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1]} {main_author[0]}, ' \
                   f'{seconde_author[1]} {seconde_author[0]}, {third_author[1]} {third_author[0]} // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'
        else:
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1]} {main_author[0]}, ' \
                   f'{seconde_author[1]} {seconde_author[0]}, {third_author[1]} {third_author[0]} // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'

    def get_gost_2(self) -> str:
        main_author = [author.strip() for author in self.get_authors()[0].split(',')]
        seconde_author = [author.strip() for author in self.get_authors()[1].split(',')]
        if self.get_journal_tom():
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1].strip()} {main_author[0]}, ' \
                   f'{seconde_author[1]} {seconde_author[0]} // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'
        else:
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1].strip()} {main_author[0]}, ' \
                   f'{seconde_author[1]} {seconde_author[0]} // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'

    def get_gost_1(self) -> str:
        main_author = [author.strip() for author in self.get_authors()[0].split(',')]
        if self.get_journal_tom():
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1]} {main_author[0]}, ' \
                   f' // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'
        else:
            return f'{self.get_authors()[0]} {self.get_article_title()} / {main_author[1]} {main_author[0]}, ' \
                   f' // {self.get_journal()}. \u2014 ' \
                   f'{self.get_year_of_article()}. \u2014 V. {self.get_journal_tom()}, \u2116 {self.get_journal_number()}. \u2014 ' \
                   f'P. {self.get_journal_pages()}.'


if __name__ == '__main__':
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