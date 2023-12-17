# user_dao.py
from flask import request, jsonify
import dbconnection as db

def create_user():
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("user_crud_pkg.create_user", [
            data['name'], data['password'], data['gender'], data['age']
        ])
        conn.commit()
        
        return jsonify({"message": "User created successfully"}), 201
def update_user(user_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        data = request.json
        cursor.callproc("user_crud_pkg.update_user", [
            user_id, data['name'], data['password'], data['gender'], data['age']
        ])
        conn.commit()
        
        return jsonify({"status": "updated"}), 200

def delete_user(user_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        cursor.callproc("user_crud_pkg.delete_user", [user_id])
        conn.commit()
        return jsonify(message='User deleted successfully'),200
    
def read_user(user_id):
    with db.create_connection() as conn, conn.cursor() as cursor:
        
        result = cursor.callfunc("user_crud_pkg.read_user", db.CURSOR, [user_id])
        user = result.fetchone()
        user_data = {
                "id": user[0], "name": user[1], "password": user[2],
                "gender": user[3], "age": user[4]
                }
        return jsonify(user_data)
def get_all_users():
    connection = db.create_connection()    
    cursor = connection.cursor()
    users_ref_cursor = cursor.callfunc('user_crud_pkg.getAllUsers', db.CURSOR)
    users_data = []
    for row in users_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(users_ref_cursor.description, row)}
        users_data.append(row_as_dict)
    return jsonify(users_data)
# 같은 방식으로 다른 DAO 함수들도 추가할 수 있습니다.
