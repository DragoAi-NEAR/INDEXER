from flask import Flask, jsonify, request
from database import get_all_tokens, get_all_pools, get_market_analysis, add_new_token, get_token_by_contract,get_holders_by_contract,get_market_analysis_by_contract,get_pools_by_contract
from logging_config import logger

app = Flask(__name__)

@app.route('/tokens', methods=['GET'])
def get_tokens():
    logger.info("Fetching all tokens")
    tokens = get_all_tokens()
    return jsonify(tokens)

@app.route('/pools', methods=['GET'])
def get_pools():
    logger.info("Fetching all pools")
    pools = get_all_pools()
    return jsonify(pools)

@app.route('/market_analysis', methods=['GET'])
def market_analysis():
    logger.info("Fetching market analysis")
    analysis = get_market_analysis()
    return jsonify(analysis)
@app.route('/pools/<contract_address>', methods=['GET'])
def get_pools_by_address(contract_address):
    logger.info(f"Fetching pools by address {contract_address}")
    pools = get_pools_by_contract(contract_address)
    if pools:
        return jsonify(pools)
    else:
        return jsonify({'error': 'No pools found for the specified contract address'}), 404

@app.route('/holders/<contract_address>', methods=['GET'])
def get_holders_by_address(contract_address):
    logger.info(f"Fetching holders by address {contract_address}")
    holders = get_holders_by_contract(contract_address)
    if holders:
        return jsonify(holders)
    else:
        return jsonify({'error': 'No holders found for the specified contract address'}), 404

@app.route('/market_analysis/<contract_address>', methods=['GET'])
def get_market_analysis_by_address(contract_address):
    logger.info(f"Fetching market analysis by address {contract_address}")
    analysis = get_market_analysis_by_contract(contract_address)
    if analysis:
        return jsonify(analysis)
    else:
        return jsonify({'error': 'No market analysis found for the specified contract address'}), 404


@app.route('/token/<contract_address>', methods=['GET'])
def get_token_by_address(contract_address):
    logger.info(f"Fetching token by address {contract_address}")
    token = get_token_by_contract(contract_address)
    if token:
        return jsonify(token)
    else:
        return jsonify({'error': 'Token not found'}), 404

@app.route('/add_token', methods=['POST'])
def add_token():
    data = request.json
    contract_address = data.get('contract_address')
    logger.info(f"Adding new token {contract_address}")
    if contract_address:
        add_new_token(contract_address)
        return jsonify({"status": "success", "message": f"Token {contract_address} added."}), 200
    else:
        logger.warning("Contract address not provided in request")
        return jsonify({"status": "error", "message": "Contract address is required."}), 400

if __name__ == '__main__':
    logger.info("Starting API server...")
    app.run(debug=True)
