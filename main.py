from src.scrape import scraper as scrape

def main():
    search = input('Search>')
    scrape.scrape(search)
    
    
main()