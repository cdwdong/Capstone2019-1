  function clock(){
				var month = new Array ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");
                var day = new Array ("Mon","Tus","Wed","Thu","Fri","Sat","Sun");
                var ampm = new Array ("AM","PM");
                var isam = 0;
                var th = "th";
                if(D==1){
                    th = "st";
                }else if(D==2){
                    th = "nd";
                }else if(D==3){
                    th = "rd";
                }else{
                    th = "th";
                }
                var date = new Date();
                var M = date.getMonth();
                var D = date.getDate();
                var d = date.getDay();
                var h = date.getHours();
                var m = date.getMinutes();
                var s = date.getSeconds();
                if(h>12||h==0){
                    h = h%12;
                    isam = 1;
                }
                h=(h>9)?h:"0"+h;
                m=(m>9)?m:"0"+m;
                s=(s>9)?s:"0"+s;
                document.getElementById("hms").innerHTML = h + ":" + m + ":" + s + " " + ampm[isam];
            }
            var timer = setInterval( function(){ clock(); }, 1000);
			
	