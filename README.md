# pylestra_scrapy_2020-02-07

## Instructions
- Create or activate a new virtualenv

- Install dependencies
```
$ pip install -r requirements.txt
```

- Run the spider
```
$ scrapy crawl imob
```

- Run the shell for debug
```
$ scrapy shell {url}
```

- Run the spider and export as .json
```
$ scrapy crawl imob -o file.json
```

- Run the spider and export as .csv
```
$ scrapy crawl imob -o file.csv
```

- Run the spider and export as .xml
```
$ scrapy crawl imob -o file.xml
```

## Reference links
[Architecture overview](https://docs.scrapy.org/en/latest/topics/architecture.html)

Learn more about css and xpath [Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)

All the [settings](https://docs.scrapy.org/en/latest/topics/settings.html)

Enjoy a [tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)

Presentation [slides](https://docs.google.com/presentation/d/1kjbGdGtlbVXzjUgnqMARgsRA8Gdy7G5v1PARVUU1cX0/edit?usp=sharing)
