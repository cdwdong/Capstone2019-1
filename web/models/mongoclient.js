var MongoClient = require('mongodb').MongoClient;
var Server = require('mongodb').Server;
var url = 'mongodb://localhost:27017/db_capstone2019';

module.exports = new MongoClient(new Server(url, 27017), {native_parser: true});