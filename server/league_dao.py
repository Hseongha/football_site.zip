from flask import  request, jsonify
import dbconnection as db



def create_league():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("league_crud_pkg.create_league", [data['tournament']])
        conn.commit()
        return jsonify({"message": "League created successfully"}), 201

def read_league(league_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        result = cursor.callfunc("league_crud_pkg.read_league", db.CURSOR, [league_id])
        league = result.fetchone()
        if league:
            league_data = {
                "id": league[0], "tournament": league[1]
            }
            return jsonify(league_data)
        else:
            return jsonify({"message": "League not found"}), 404

def update_league(league_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("league_crud_pkg.update_league", [league_id, data['tournament']])
        conn.commit()
        return jsonify({"status": "updated"}), 200

def delete_league(league_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("league_crud_pkg.delete_league", [league_id])
        conn.commit()
        return jsonify(message='League deleted successfully'), 200


