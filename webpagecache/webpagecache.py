import time
import requests
from wire import database

class WebpageCache(object):
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"

    def __init__(self, cache_filename, wait_before_dl = 0):
        self.db = database.Database(cache_filename)
        self.db.row_factory = database.sqlite3.Row
        self.setup_content_table()
        self.wait_before_dl = wait_before_dl

    def setup_content_table(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS content (
            url TEXT PRIMARY KEY,
            content TEXT )''')

    def get_page(self, url):
        row = self.db.select("content", columns = ["content"], equal = {"url": url}).fetchone()
        if row:
            html = row["content"]
        else:
            if self.wait_before_dl:
                time.sleep(self.wait_before_dl)
            page = requests.get(url, headers={"User-Agent": WebpageCache.USER_AGENT})
            html = page.text
            self.db.insert("content", url = url, content = html)
        return html
