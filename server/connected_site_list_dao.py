from flask import request, jsonify
import dbconnection as db


def create_connected_site():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("connected_site_list_crud_pkg.create_connected_site", [
            data['match_id'], data['connected_site'], data['connected_site_link']
        ])
        conn.commit()
        return jsonify({"message": "Connected site information created successfully"}), 201

def read_connected_site(connected_site_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        result = cursor.callfunc("connected_site_list_crud_pkg.read_connected_site", db.CURSOR, [connected_site_id])
        connected_site_info = result.fetchone()
        if connected_site_info:
            connected_site_data = {
                "id": connected_site_info[0], "match_id": connected_site_info[1],
                "connected_site": connected_site_info[2], "connected_site_link": connected_site_info[3]
            }
            return jsonify(connected_site_data)
        else:
            return jsonify({"message": "Connected site information not found"}), 404

def update_connected_site(connected_site_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("connected_site_list_crud_pkg.update_connected_site", [
            connected_site_id, data['connected_site'], data['connected_site_link']
        ])
        conn.commit()
        return jsonify({"status": "updated"}), 200

def delete_connected_site(connected_site_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("connected_site_list_crud_pkg.delete_connected_site", [connected_site_id])
        conn.commit()
        return jsonify(message='Connected site information deleted successfully'), 200


