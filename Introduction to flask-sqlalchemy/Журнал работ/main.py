from flask import Flask, render_template
from data import db_session
import datetime
from data.actions import Actions


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


@app.route("/")
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    # action = Actions()
    # action.title_activity = "Deployment of residential modules 1 and 2"
    # action.team_leader = "Elmir Ahmadullin"
    # action.duration = "15 hours"
    # action.lst_collaborators = "2, 3"
    # action.is_finished = True
    # db_sess.add(action)
    #
    # action = Actions()
    # action.title_activity = "Explonation of mineral resources"
    # action.team_leader = "Scott Jhonson"
    # action.duration = "15 hours"
    # action.lst_collaborators = "4, 3"
    # action.is_finished = False
    # db_sess.add(action)
    #
    # action = Actions()
    # action.title_activity = "Development of a managment system"
    # action.team_leader = "Sanders Teddy"
    # action.duration = "25 hours"
    # action.lst_collaborators = "5"
    # action.is_finished = True
    # db_sess.add(action)
    # db_sess.commit()

    return render_template("works_log.html", actions=db_sess.query(Actions).all())


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
