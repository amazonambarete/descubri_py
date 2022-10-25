import app

def build_places_query (args):

    query = app.Lugares.query
    if ('category' in args.keys()):
        query = query.filter_by(category = args['category'])
    if ('tecnaso' in args.keys()):
        query = query.filter_by(wifi = args['tecnaso'])
    if ('departamento' in args.keys()):
        query = query.filter_by(wifi = args['departamento'])
    if ('accessible_bathroom' in args.keys()):
        query = query.filter_by(wifi = args['accessible_bathroom'])
    if ('ramp_access' in args.keys()):
        query = query.filter_by(wifi = args['ramp_access'])
    if ('pool' in args.keys()):
        query = query.filter_by(wifi = args['pool'])
    if ('wifi' in args.keys()):
        query = query.filter_by(wifi = args['wifi'])
    if ('dining' in args.keys()):
        query = query.filter_by(wifi = args['dining'])
    if ('card' in args.keys()):
        query = query.filter_by(wifi = args['card'])
    if ('pickup_service' in args.keys()):
        query = query.filter_by(wifi = args['pickup_service'])
    return query