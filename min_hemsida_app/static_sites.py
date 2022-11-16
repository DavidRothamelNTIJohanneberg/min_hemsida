from flask import Blueprint, flash, g, redirect, render_template, request, url_for

bp = Blueprint("sites", __name__)

@bp.route("/mina_hemsidor")
def hemsidor():
    return render_template('mina_hemsidor.html')

@bp.route("/mina_projekt")
def projekt():
    return render_template('mina_projekt.html')

@bp.route("/om_mig")
def om_mig():
    return render_template('om_mig.html')