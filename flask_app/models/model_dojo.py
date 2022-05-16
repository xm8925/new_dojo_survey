# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.gender = data['gender']
        self.subscribe = data['subscribe']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

# C
    @classmethod
    def create(cls, data:dict) -> object:
        """
        inserting data into the dojos table
        this is the request.form
        """
        #query string
        query = "INSERT INTO dojos(name, location, language, comment, gender, subscribe) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, %(gender)s, %(subscribe)s)"
        #contact the DB
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        # return
        return dojo_id


# R
    @classmethod
    def get_last(cls):
        """
        selecting one from the dojos table
        """
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        if results:
            return cls(results[0])
        return False
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must have at least 3 characters.", "error_user_name")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Buddy you got to choose a location.", "error_user_location")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Forgot to pick a language.", "error_user_language")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Put at least 10 letter in there.", "error_user_comment")
            is_valid = False
        return is_valid