from flask import request, render_template, make_response
from datetime import datetime
from flask import current_app as app
from .models import db, user, treasure, own, market

@app.route('/', methods-['GET'])
def create_db():
    db.drop_all()
    t1=treasure('t1', luck=0, work=50, price=50)
    db.session.add(t1)
    t2=treasure('t2', 0, 100, 100)
    db.session.add(t2)
    t3=treasure('t3', 0, 150, 150)
    db.session.add(t3)
    t4=treasure('t4', 60, 0, 60)
    db.session.add(t4)
    t5=treasure('t5',30, 0, 30)
    db.session.add(t5)
    t6=treasure('t6', 20, 0 ,20)
    db.session.add(t6)
    t7=treasure('t7',0, 40, 40)
    db.session.add(t7)
    t8=treasure('t8',80, 0, 80)
    db.session.add(t8)
    u1=user(uid='u1', money=0, luck=0, work=0)
    u2=user(uid='peggy', money=80, luck=40,work=10)
    u3=user(uid='doge', money=120, luck=20,work=40)  
    db.session.add(u1) 
    db.session.add(u2)
    db.session.add(u3)
    o1=market(tid='t6',seller='peggy')
    o2=market(tid='t7',seller='u1')
    o3=market(tid='t8',seller='doge')
    db.session.add(o1)
    db.session.add(o2)
    db.session.add(o3)
    db.session.commit()

    return make_response("db created!")