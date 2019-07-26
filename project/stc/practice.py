
Company = {
    "article_labels": [
        "Apple",
        "XLF",
        "SPY",
        "QQQQ"
    ],
    "article_data": [
        5,
        7,
        8,
        10
    ]
}

data = {
            "article_labels": Company.keys(),
            "article_data": Company.values(),
        }

print(data)

def get(self, format=None):
        articles = dict()
        #information from .models
        for company in Company.items():
            print(company)
   
get(Company)


Close = {
    "article_labels": [
        "Apple",
        "XLF",
        "SPY",
        "QQQQ"
    ],
    "article_data": [
        5,
        7,
        8,
        10
    ]
}

data = {
            "article_labels": Company.keys(),
            "article_data": Company.values(),
        }

print(data)

d = {'a':(1,90),'b':(2,80),'c':(3, 60)}
d = [v[0] for v in d.values()]
print(d)