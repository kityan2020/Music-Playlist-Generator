from flask import Flask, jsonify, request, render_template
import spotify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Main.html', artiststuff="")
@app.route('/api/search', methods=['GET', "POST"])
def search():
    query = request.args.get('q')
    results = spotify.Playlist(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
