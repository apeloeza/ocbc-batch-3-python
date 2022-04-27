"""
This is the director module and supports all the REST actions for the
director data
"""

from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie


def read_all():
    """
    This function responds to a request for /api/director
    with the complete lists of director

    :return:        json string of list of director
    """
    # Create the list of director from our data
    director = Director.query.order_by(db.desc(Director.id)).limit(20).all()

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data


def by_gender(director_gender):
    """
    This function responds to a request for /api/director/{person_id}
    with one matching person from director

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    
    director = Director.query.filter(Director.gender == director_gender).order_by(db.desc(Director.id)).limit(20).all()
    # director = (
    #     Director.query.filter(Director.gender == director_gender)
    #     .outerjoin(Movie)
    #     .one_or_none()
    # )

    # Did we find a person?
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data

def by_department(department):
    """
    This function responds to a request for /api/director/{person_id}
    with one matching person from director

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    
    search = "%{}%".format(department)
    director = Director.query.filter(Director.department.like(search)).all()

    # Did we find a person?
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data

def by_name(director_name):
    """
    This function responds to a request for /api/director/{person_id}
    with one matching person from director

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    
    search = "%{}%".format(director_name)
    director = Director.query.filter(Director.name.like(search)).all()

    # Did we find a person?
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data


def read_one(director_id):
    """
    This function responds to a request for /api/director/{person_id}
    with one matching person from director

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    director = (
        Director.query.filter(Director.id == director_id)
        .outerjoin(Movie)
        .one_or_none()
    )

    # Did we find a person?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {director_id}")


def create(director):
    """
    This function creates a new person in the director structure
    based on the passed in person data

    :param person:  person to create in director structure
    :return:        201 on success, 406 on person exists
    """
    name = director.get("name")
    gender = director.get("gender")
    uid = director.get("uid")
    department = director.get("department")

    existing_director = (
        Director.query.filter(Director.name == name)
        .filter(Director.uid == uid)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_director is None:

        # Create a person instance using the schema and the passed in person
        schema = DirectorSchema()
        new_direct = schema.load(director, session=db.session)

        # Add the person to the database
        db.session.add(new_direct)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_direct)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f"Director {name} with UID {uid} exists already")


def update(director_id, director):
    """
    This function updates an existing person in the director structure

    :param person_id:   Id of the person to update in the director structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_direct = Director.query.filter(
        Director.id == director_id
    ).one_or_none()

    # Did we find an existing person?
    if update_direct is not None:

        # turn the passed in person into a db object
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)

        # Set the id to the person we want to update
        update.id = update_direct.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_direct)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {director_id}")


def delete(director_id):
    """
    This function deletes a person from the director structure

    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    director = Director.query.filter(Director.id == director_id).one_or_none()

    # Did we find a person?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {director_id} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {director_id}")