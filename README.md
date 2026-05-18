# 🎬 Movie Info Finder

A simple command-line app that fetches movie details for any film — just type a title and get instant info straight from the OMDb database.

## 📸 Sample Output

```
Enter movie name: Inception

🎬 Title       : Inception
📅 Year        : 2010
⭐ IMDb Rating : 8.8
🎭 Genre       : Action, Adventure, Sci-Fi
👨‍👩‍👧‍👦 Actors      : Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page
📝 Plot        : A thief who steals corporate secrets through the use of
                 dream-sharing technology is given the inverse task of
                 planting an idea into the mind of a C.E.O.
```

---

## ⚡ Quick Setup (5 minutes)

### Step 1 — Clone the repo

```bash
git clone https://github.com/your-username/movie-info-finder.git
cd movie-info-finder
```

### Step 2 — Install dependencies

```bash
pip install requests python-dotenv
```

### Step 3 — Get a free API key

1. Sign up at 👉 [omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Choose the **FREE tier** (1,000 requests/day)
3. Check your email and **click the activation link**
4. Copy your key

> ⚠️ If you're using a Hotmail/Outlook/Yahoo email, the key email may be delayed. Use Gmail if possible.

### Step 4 — Create a `.env` file

In the project folder, create a file named `.env` and add:

```
OMDB_API_KEY=paste_your_key_here
```

### Step 5 — Run it!

```bash
python movie_info_finder.py
```

Then just enter any movie title when prompted. That's it! 🎉

---

## ❓ Troubleshooting

**"Movie not found"**
→ Double check the spelling. Try the full official title e.g. `The Dark Knight` instead of `Dark Knight`

**"The request timed out"**
→ Your connection may be slow. Try again in a moment

**"Network error"**
→ Check your internet connection and try again

**API key not working?**
→ New OMDb keys need to be activated via email first. Also check your spam folder!

---

## 📦 Requirements

- Python 3.x
- `requests`
- `python-dotenv`

Or install everything at once:

```bash
pip install -r requirements.txt
```

> A `requirements.txt` is included in the repo for convenience.

---

## 📁 Project Structure

```
movie-info-finder/
├── movie_info_finder.py   # Main script
├── .env                   # Your API key (you create this, never shared)
├── .env.example           # Template showing what goes in .env
├── .gitignore             # Keeps your .env off GitHub
├── requirements.txt       # Dependencies
└── README.md
```