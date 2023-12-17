from flask import request, jsonify
import dbconnection as db


def create_team():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("team_crud_pkg.create_team", [
            data['name'], data['league'], data['emblem']
        ])
        conn.commit()
        return jsonify({"message": "Team created successfully"}), 201

def update_team(team_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("team_crud_pkg.update_team", [
            team_id, data['name'], data['league'], data['emblem']
        ])
        conn.commit()
        return jsonify({"status": "updated"}), 200

def delete_team(team_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("team_crud_pkg.delete_team", [team_id])
        conn.commit()
        return jsonify(message='Team deleted successfully'), 200

def read_team(team_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        result = cursor.callfunc("team_crud_pkg.read_team", db.CURSOR, [team_id])
        team = result.fetchone()
        if team:
            team_data = {
                "id": team[0], "name": team[1], "league": team[2], "emblem": team[3]
            }
            return jsonify(team_data)
        else:
            return jsonify({"message": "Team not found"}), 404



