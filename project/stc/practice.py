
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