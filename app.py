from app import app
from app.controllers.quote_controller import QuoteController
from app.controllers.user_controller import UserController
from app.controllers.admin_controller import AdminController
from flask import request

# Routes for fetching stock data
@app.route('/get_ltp', methods=['GET'])
def get_ltp():
    instrument_identifier = request.args.get('instrument_identifier')
    return QuoteController.get_ltp(instrument_identifier)

@app.route('/get_all_instrument_identifiers', methods=['GET'])
def get_all_instrument_identifiers():
    return QuoteController.get_all_instrument_identifiers()

# Routes for user apis
@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@app.route('/register', methods=['POST'])
def register():
    return UserController.register()

@app.route('/buy', methods=['POST'])
def buy():
    return UserController.buy()

@app.route('/sell', methods=['POST'])
def sell():
    return UserController.sell()

@app.route('/user/<user_id>/purchase_history', methods=['GET'])
def get_purchase_history(user_id):
    return UserController.get_purchase_history(user_id)

@app.route('/user/<user_id>/sell_history', methods=['GET'])
def get_sell_history(user_id):
    return UserController.get_sell_history(user_id)

@app.route('/user/<user_id>/favorite_symbols', methods=['POST'])
def add_favorite_symbols(user_id):
    return UserController.add_favorite_symbols(user_id)

@app.route('/user/<user_id>/favorite_symbols', methods=['GET'])
def get_favorite_symbols(user_id):
    return UserController.get_favorite_symbols(user_id)

@app.route('/user/<user_id>/delete_favorite_symbols', methods=['POST'])
def delete_favorite_symbols(user_id):
    return UserController.delete_favorite_symbols(user_id)

# Routes for admin apis
@app.route('/create_admin', methods=['POST'])
def create_admin():
    return AdminController.create_admin()

@app.route('/create_user', methods=['POST'])
def create_user():
    return AdminController.create_user()

@app.route('/pause_user', methods=['POST'])
def pause_user():
    return AdminController.pause_user()

@app.route('/ban_user', methods=['POST'])
def ban_user():
    return AdminController.ban_user()

@app.route('/get_user_history/<user_id>', methods=['GET'])
def get_user_history(user_id):
    return AdminController.get_user_history(user_id)


if __name__ == '__main__':
    app.run(debug=True)