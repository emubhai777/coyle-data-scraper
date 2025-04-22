from flask import Flask, send_file, render_template
import pandas as pd
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_file():
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.login.coylextrading.com/dl/6471c6/s/c51594/r/KJekHIprQ0aN81PMKwFyRw',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'GoogleAccessId': 'gcs-url-signer@glide-prod.iam.gserviceaccount.com',
        'Expires': '1745306239',
        'Signature': 'WDbQmeSCkVbvRWuWyK3vf0qO/LKfkG45b6i3V8wEs4mYNKrbAAgt91XIPHnwC/K2zwb+LdfP+aLeIwuTlfj1cvJEgT3TfQ5kWxESlA9Jm9BqJXZoFOfk1K06DjR7XASv391OEjwpwsA46diIT/sdj6E/8nnOKx9azdTKKLhJETKfOhU38EnwZH3k5AZgDBSIdbaVcGB6ljBACzyLkjj9wSt6Iv6iy2b4PHZOXsNSPnEwfIySin5HRBAb/VaqO4LQ8ASv1U+30gcOWGabvdSb+MHT6gkHJCpZMHnlIBIeCTQ5kyL/QDG1gv7cWYmTFv1jHPTTyL0MxdiSAB824/8Fzg=='
    }

    response = requests.get(
        'https://www.login.coylextrading.com/data/snapshots-native-table/RO051c0wKsFm5WyLDseL.jzon',
        params=params,
        headers=headers,
    ).json()

    df = pd.json_normalize(response['rows'])

    filename = f"coylextrading_{datetime.now().strftime('%b-%d-%Y')}.xlsx"
    df.to_excel(filename, index=False)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
