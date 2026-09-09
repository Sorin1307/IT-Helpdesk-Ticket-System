from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tickets = []


@app.route("/")
def index():
    return render_template("index.html", tickets=tickets)


@app.route("/create", methods=["POST"])
def create_ticket():
    ticket = {
        "id": len(tickets) + 1,
        "title": request.form["title"],
        "description": request.form["description"],
        "priority": request.form["priority"],
        "status": "Open",
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tickets.append(ticket)
    return redirect(url_for("index"))


@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = request.form["status"]
            break

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
