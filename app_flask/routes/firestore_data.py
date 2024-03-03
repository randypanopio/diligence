"""
    routes that use the firestore db
"""
from datetime import datetime
from flask import jsonify, Blueprint, request, abort
from firestore.database import db_manager
from config import ACTIVE_API_VERSION, DAY_FORMAT

firestore_data_bp = Blueprint("database", __name__)

@firestore_data_bp.route(f'{ACTIVE_API_VERSION}stocks_data', methods=['GET'])
def get_historic_data():
    """
        TODO docstring
    """
    if request.args.get('ticker') not in db_manager.get_available_tickers():
        abort(404, description={'error': "ticker not found"})

    try:
        date_start = datetime.strptime(request.args.get('date_start'), DAY_FORMAT)
        date_end = datetime.strptime(request.args.get('date_start'), DAY_FORMAT)
    except ValueError:
        message = "something"
        print(message)
        abort(404, description={'error': message})

    # TODO use me to check health, EG if other external api i would be usingis available, if db is avail, etc.
    data = {'message': f'{ACTIVE_API_VERSION} API is available'}
    return jsonify(data)

def get_daily_banner_messages():
    '''
        Retrieves randomized set of available banner messages    
    '''
    # generate today's seed

    # retrieve length of available message


    # get the random messages based on the seed

    # connect to db and retrieve 
