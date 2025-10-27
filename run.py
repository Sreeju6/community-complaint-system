from app import create_app, db   # adjust if you already have app defined somewhere
from flask import Flask

app = create_app()

# ✅ Temporary initdb route to create tables
@app.route("/initdb")
def initdb():
    try:
        db.create_all()
        return "✅ Tables created successfully!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
