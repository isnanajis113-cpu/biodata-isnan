from flask import Flask

app = Flask(__name__)

@app.route('/')
def biodata():
    return '''
    <html>
    <head>
        <title>Biodata Nanzz</title>
        <style>
            body { background: #111; color: white; font-family: Arial; text-align: center; }
            .card { background: #222; width: 350px; margin: 50px auto; padding: 30px; border-radius: 20px; }
            img { width: 150px; height: 150px; border-radius: 50%; border: 3px solid #00ff00; object-fit: cover; }
            h1 { color: #00ff00; }
            .kotak { background: #333; padding: 10px; border-radius: 10px; margin: 10px; text-align: left; }
            button { background: #00ff00; border: none; padding: 10px 20px; border-radius: 10px; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/static/FOTO2.JPG">
            <h1>Nanzz</h1>
            <p>TEBO | Calon Syber Securty, Indonesia</p>
            <div class="kotak">
                <b>Umur:</b> 16 Tahun<br>
                <b>Sekolah:</b> SMKN 2 TEBO<br>
                <b>Hobi:</b> Coding<br>
                <b>Cita-cita:</b> Progammer 
            </div>
            <p>WEb Nanzz</p>
            <button onclick="alert('Halo! Makasih udah mampir ke webku!')">Sapa Aku!</button>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)