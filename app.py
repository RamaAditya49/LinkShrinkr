from flask import Flask, redirect, request, render_template
import sqlite3 # Ensure sqlite3 is imported if not already
import hashlib # Ensure hashlib is imported if not already

DATABASE_NAME = 'urls.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            clicks INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_url(original_url, short_code):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO urls (original_url, short_code)
            VALUES (?, ?)
        ''', (original_url, short_code))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_url(short_code):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT original_url FROM urls
        WHERE short_code = ?
    ''', (short_code,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def increment_click_count(short_code):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE urls
        SET clicks = clicks + 1
        WHERE short_code = ?
    ''', (short_code,))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    return updated_rows > 0

def generate_short_code(long_url):
    encoded_url = long_url.encode('utf-8')
    hash_object = hashlib.sha256(encoded_url)
    hex_dig = hash_object.hexdigest()
    return hex_dig[:6]

app = Flask(__name__)

@app.route('/<string:short_code>')
def redirect_to_url(short_code):
    original_url = get_url(short_code)
    if original_url:
        increment_click_count(short_code)
        # Ensure the URL has a scheme, otherwise Flask redirect might treat it as a relative path
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url
        return redirect(original_url)
    else:
        return "URL not found", 404

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if not long_url:
            error = "URL cannot be empty."
            return render_template('index.html', error=error)

        # Basic validation for URL format
        if not (long_url.startswith('http://') or long_url.startswith('https://')):
            long_url = 'http://' + long_url

        short_code = generate_short_code(long_url)

        # Loop to find a unique short_code (simple collision handling)
        # In a high-traffic system, a more robust unique ID generation is needed.
        MAX_TRIES = 10
        tries = 0
        while get_url(short_code) is not None: # Check if short_code already exists
            tries += 1
            if tries >= MAX_TRIES:
                error = "Could not generate a unique short code. Please try again."
                return render_template('index.html', error=error)
            short_code = generate_short_code(long_url + str(tries)) # Alter input to get new hash

        if add_url(long_url, short_code):
            # Fetch the newly created entry to get the click count (should be 0)
            # This is a bit inefficient, could be optimized.
            # For now, we don't have a get_url_details function, so we'll pass 0.
            # We also need the full URL for the template
            full_short_url = request.host_url + short_code
            return render_template('index.html', short_url=full_short_url, original_url=long_url, clicks=0)
        else:
            # This case should ideally be rare with the collision handling above
            error = "Failed to save URL. The short code might already exist or another database error occurred."
            return render_template('index.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    init_db() # Ensure DB is initialized
    app.run(debug=True)
