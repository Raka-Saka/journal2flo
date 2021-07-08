from django.shortcuts import render


def home(request):
    import requests
    import json

    # Grab crypto price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ADA,XCH,SHIB,ALGO&tsyms=USD,JPY")
    price = json.loads(price_request.content)


    # Grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote +"&tsyms=USD,JPY")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a valid crypto currency symbol into the form."
        return render(request, 'prices.html', {'notfound': notfound})
