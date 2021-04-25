#!/usr/bin/env python


import json
import uuid
from datetime import datetime, timedelta
from random import randint, shuffle

import names
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return ""


@app.route("/facts", methods=["GET"])
def facts():
    return jsonify(_shuffle(facts()))


def facts():
    facts = []

    with open("facts.txt") as file:
        for line in file:
            fact = {
                "cuid": str(uuid.uuid4()),
                "first_name": names.get_first_name(),
                "last_name": names.get_last_name(),
                "date_of_birth": _date_of_birth(maximum_age=24),
                "fact": line.strip(),
            }

            facts.append(fact)

    return facts


def _shuffle(array):
    shuffled_array = array
    shuffle(shuffled_array)
    return shuffled_array


def _date_of_birth(maximum_age=99, date_format="%Y-%m-%d"):
    return (datetime.today() - timedelta(days=randint(0, 365 * maximum_age))).strftime(
        date_format
    )


if __name__ == "__main__":
    app.run(debug=True)
