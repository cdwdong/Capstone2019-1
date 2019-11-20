var express = require('express');
var router = express.Router();
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var QUERY_LIMIT = 259200;

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index.html');
});

router.get('/sensor', function(req, res, next) {
    res.set('Content-Type', 'text/plain');
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
        var dbo = db.db("db_capstone2019");
        var where;
        var select = {};

        
        where = dbo.collection("sensor_data").find({});
        
        if(req.query.limit && !isNaN(req.query.limit) && Number.isSafeInteger(req.query.limit)) {
            where = where.limit(Number(req.query.limit));
        }
        else{
            where = where.limit(QUERY_LIMIT);
        }
        where.toArray(function(err, result) {
            if (err) throw err;
            res.send(result);
            db.close();
        });
        
    });
});



module.exports = router;
