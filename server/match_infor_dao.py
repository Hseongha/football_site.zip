from flask import request, jsonify
import dbconnection as db


def create_match():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("match_infor_crud_pkg.create_match", [
            data['home_team'], data['away_team'], data['league_id'],
            data['match_number'], data['dates'], data['times']
        ])
        conn.commit()
        return jsonify({"message": "Match information created successfully"}), 201

def read_match(match_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        result = cursor.callfunc("match_infor_crud_pkg.read_match", db.CURSOR, [match_id])
        match_info = result.fetchone()
        if match_info:
            match_data = {
                "id": match_info[0], "home_team": match_info[1], "away_team": match_info[2],
                "league_id": match_info[3], "match_number": match_info[4],
                "dates": match_info[5].strftime('%Y-%m-%d'), "times": match_info[6].strftime('%H:%M:%S')
            }
            return jsonify(match_data)
        else:
            return jsonify({"message": "Match information not found"}), 404

def update_match(match_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("match_infor_crud_pkg.update_match", [
            match_id, data['home_team'], data['away_team'], data['league_id'],
            data['match_number'], data['dates'], data['times']
        ])
        conn.commit()
        return jsonify({"status": "updated"}), 200

def delete_match(match_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("match_infor_crud_pkg.delete_match", [match_id])
        conn.commit()
        return jsonify(message='Match information deleted successfully'), 200



