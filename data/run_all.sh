#!/bin/bash

rm app.db
python create_database.py
python seeder.py