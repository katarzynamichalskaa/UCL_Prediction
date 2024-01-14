from bs4 import BeautifulSoup
from GetContent import GetContent

class AssociationRanking(GetContent):

    def scrape(self, nationality):

        content = self.get_content()
        rank_list = []

        if content:

            soup = BeautifulSoup(content, 'lxml')
            table = soup.find('table', class_='t1')
            rows = table.find_all('tr', class_='countryline')

            for row in rows:

                country = row.find('td', style='text-align: left;').text.strip()

                if country == nationality:

                    ranks = row.find_all('td')

                    for rank in ranks:

                        rank_list.append(rank.text.strip())

                    raw_rank = rank_list[len(rank_list) - 2]
                    return raw_rank



