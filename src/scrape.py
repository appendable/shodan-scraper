import shodan, io

key = 'nu4C4LUsjuJX0njhtrXsCRCyiHlPZH0B'

class scraper:
    def scrape(query):
        api = shodan.Shodan(key)
        try:
            results = api.search(query)
            print('Results found: {}'.format(results['total']))
            with io.open('scraper-output.txt', 'w', encoding='utf-8') as op:
                for result in results['matches']:
                    op.write('IP: {}'.format(result['ip_str']))
                    op.write(result['data'])
        except shodan.APIError as e:
            print('Error: {}'.format(e))
        