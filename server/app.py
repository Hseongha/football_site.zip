from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import users_dao as users  # dao 모듈을 import
import team_dao as team
import prefer_team_dao as prefer_team
import league_dao as league
import match_infor_dao as match_infor
import connected_site_list_dao as connected_site_list
import dbconnection as db

app = Flask(__name__)
CORS(app, origins="*")
app.config.from_object(__name__)

#users
app.add_url_rule('/create_user', view_func=users.create_user, methods=['POST'])
app.add_url_rule('/update_user/<int:user_id>', view_func=users.update_user, methods=['PUT'])
app.add_url_rule('/delete_user/<int:user_id>', view_func=users.delete_user, methods=['DELETE'])
app.add_url_rule('/read_user/<int:user_id>', view_func=users.read_user, methods=['GET'])
app.add_url_rule('/get_all_users', view_func=users.get_all_users, methods=['GET'])
#team
app.add_url_rule('/create_team', view_func=team.create_team, methods=['POST'])
app.add_url_rule('/update_team/<int:team_id>', view_func=team.update_team, methods=['PUT'])
app.add_url_rule('/delete_team/<int:team_id>', view_func=team.delete_team, methods=['DELETE'])
app.add_url_rule('/read_team/<int:team_id>', view_func=team.read_team, methods=['GET'])
#prefer_team
app.add_url_rule('/add_preferred_team', view_func=prefer_team.add_preferred_team, methods=['POST'])
app.add_url_rule('/get_preferred_team/<int:user_id>', view_func=prefer_team.get_preferred_teams, methods=['GET'])
app.add_url_rule('/remove_preferred_team/<int:user_id>/<int:team_id>', view_func=prefer_team.remove_preferred_team, methods=['DELETE'])
#league
app.add_url_rule('/create_league', view_func=league.create_league, methods=['POST'])
app.add_url_rule('/read_league/<int:league_id>', view_func=league.read_league, methods=['GET'])
app.add_url_rule('/update_league/<int:league_id>', view_func=league.update_league, methods=['PUT'])
app.add_url_rule('/delete_league/<int:league_id>', view_func=league.delete_league, methods=['DELETE'])
#match_infor
app.add_url_rule('/create_match', view_func=match_infor.create_match, methods=['POST'])
app.add_url_rule('/read_match/<int:match_id>', view_func=match_infor.read_match, methods=['GET'])
app.add_url_rule('/update_match/<int:match_id>', view_func=match_infor.update_match, methods=['PUT'])
app.add_url_rule('/delete_match/<int:match_id>', view_func=match_infor.delete_match, methods=['DELETE'])
#connected_site_list
app.add_url_rule('/create_connected_site', view_func=connected_site_list.create_connected_site, methods=['POST'])
app.add_url_rule('/read_connected_site/<int:connected_site_id>', view_func=connected_site_list.read_connected_site, methods=['GET'])
app.add_url_rule('/update_connected_site/<int:connected_site_id>', view_func=connected_site_list.update_connected_site, methods=['PUT'])
app.add_url_rule('/delete_connected_site/<int:connected_site_id>', view_func=connected_site_list.delete_connected_site, methods=['DELETE'])


@app.route('/')
def index():
    return jsonify('Hello!')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/get_team_match',methods=['GET'])
def get_team_match():
    connection = db.create_connection()
    cursor = connection.cursor()
    join_ref_cursor = cursor.callfunc("GetTeamMatch", db.CURSOR)
    join_data = []
    for row in join_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(join_ref_cursor.description, row)}
        join_data.append(row_as_dict)
    return jsonify(join_data)
    
@app.route('/get_user_prefer',methods=['GET'])
def get_user_prefer():
    connection = db.create_connection()
    cursor = connection.cursor()
    join_ref_cursor = cursor.callfunc("GetUserPrefer", db.CURSOR)
    join_data = []
    for row in join_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(join_ref_cursor.description, row)}
        join_data.append(row_as_dict)
    return jsonify(join_data)
@app.route('/get_match_site',methods=['GET'])
def get_match_site():
    connection = db.create_connection()
    cursor = connection.cursor()
    join_ref_cursor = cursor.callfunc("GetMatchSite", db.CURSOR)
    join_data = []
    for row in join_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(join_ref_cursor.description, row)}
        join_data.append(row_as_dict)
    return jsonify(join_data)








if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
 