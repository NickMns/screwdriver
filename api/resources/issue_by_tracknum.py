from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, marshal
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

import datetime
import uuid

from app import db
from models import models

from resources.fields import issues_fields

class IssueFindByTrackNumAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("track_num_list", type=str, action="append")
        super(IssueFindByTrackNumAPI, self).__init__()

    #@jwt_required
    @swag_from("apidocs/issues_by_tracknum_get.yml")
    def get(self):
        args = self.reqparse.parse_args()
        print(args["track_num_list"])
        if args["track_num_list"] is None:
            return {"message": "No arguments passed"}, 400
        tracknum_list = args["track_num_list"][0].split(",")
        print(tracknum_list)
        issues = models.Issues.query.filter(models.Issues.Issue_Track_Num.in_(tracknum_list)).all() #Query database
            
        print(issues)
        return {'Issues': [marshal(issue, issues_fields) for issue in issues]}