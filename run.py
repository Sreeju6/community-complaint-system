from app import db, app

@app.route("/initdb")
def initdb():
    try:
        db.create_all()
        return "✅ All tables created successfully!"
    except Exception as e:
        return f"❌ Error creating tables: {e}"
