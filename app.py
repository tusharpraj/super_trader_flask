from app import app
from app.controllers.quote_controller import QuoteController
from app.controllers.user_controller import UserController
from flask import request

# Routes

# Routes for fetching stock data
@app.route('/get_ltp', methods=['GET'])
def get_ltp():
    instrument_identifier = request.args.get('instrument_identifier')
    return QuoteController.get_ltp(instrument_identifier)

@app.route('/get_all_instrument_identifiers', methods=['GET'])
def get_all_instrument_identifiers():
    return QuoteController.get_all_instrument_identifiers()

# Routes for user authentication and stock trading
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


if __name__ == '__main__':
    app.run(debug=True)