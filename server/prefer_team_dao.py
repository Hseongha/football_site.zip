from flask import request, jsonify
import dbconnection as db

def add_preferred_team():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("prefer_team_crud_pkg.add_preferred_team", [
            data['user_id'], data['team_id']
        ])
        conn.commit()
        return jsonify({"message": "Preferred team added successfully"}), 201

def get_preferred_teams(user_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        result = cursor.callfunc("prefer_team_crud_pkg.get_preferred_teams", db.CURSOR, [user_id])
        teams = result.fetchall()
        preferred_teams = []
        for team in teams:
            preferred_teams.append({
                "id": team[0], "name": team[1], "league": team[2], "emblem": team[3]
            })
        return jsonify(preferred_teams)

def remove_preferred_team(user_id, team_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("prefer_team_crud_pkg.remove_preferred_team", [user_id, team_id])
        conn.commit()
        return jsonify(message='Preferred team removed successfully'), 200



