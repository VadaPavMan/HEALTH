from flask import Blueprint, render_template, request

search_bp = Blueprint('search', __name__)

@search_bp.route('/')
def search():
    query = request.args.get('query', '')
    # Placeholder for search logic
    results = []
    return render_template('search.html', query=query, results=results)
