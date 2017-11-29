var express = require('express');
var app = express();
app.use(express.static('.'));
var cors = require('cors');
app.use(cors());
port = 5000;
var exec = require('child_process').exec;
var songIndex = 0;
var pid = "";
var listLength = null;
songList = [];


exec("ls | grep .mp3", function(error, stdout, stderr) {
	if(error){
		console.log(error);
	}
	else{
		songList = stdout.split("\n");
		console.log("LIST OF SONGS : \n")
			for (var i = songList.length - 2; i >= 0; i--) {
				console.log(i + " : " + songList[i] + "\n");
			}
			//console.log(stdout);
			listLength = songList.length-2;



	console.log("LENGTH : " + listLength)

	app.get('/' , function(req,res){
		res.sendFile(__dirname + '/music.html');
	})

	app.get('/playsong' , function(req , res){
		var song = playSong(songIndex);
		console.log("SENDING SONG " + song);
		res.send(song);
	})

	app.get('/stopsong' , function(req , res){
		stopSong();
	})

	app.get('/nextsong', function(req , res){
		var song = nextSong();
		res.send(song);
	})

	app.get('/lastsong' , function(req , res){
		var song = previousSong();
		res.send(song);
	})

	app.get('/volumeup' , function(req , res){
				exec("amixer -D pulse sset Master 10%+", function(error, stdout, stderr) {
			if(error){
				console.log(error);
			}
			else{
				console.log("VOL +");
			}
		});
	})

	app.get('/volumedown' , function(req , res){
				exec("amixer -D pulse sset Master 10%-", function(error, stdout, stderr) {
			if(error){
				console.log(error);
			}
			else{
				console.log("VOL -");
			}
		});
	})

	function playSong(songIndex){
		console.log("Playing : " + songList[songIndex%listLength] + "\n");
		var cmd = 'mplayer ' + songList[songIndex%listLength];
		exec(cmd, function(error, stdout, stderr) {
			if(error){
				// console.log("ERROR");
			}
			else{
				//console.log(stdout);
				
			}
		});
		return songList[songIndex%listLength];
	}

	function stopSong(){
		var pid = "";
		exec("ps -aux | grep mplayer", function(error, stdout, stderr) {
			if(error){
				//console.log(error);
			}
			else{
				outString = stdout.split(" ");

				for (var i = outString.length - 2; i >= 0; i--) {
					console.log(i + " : " + outString[i] + "\n");
				}

				pid = outString[31];
				//console.log(stdout);
				killCmd = "kill -9 "+pid;
				exec(killCmd, function(error, stdout, stderr) {
				});

				console.log("stoping PID : " + pid);
			}
		});
	}

	function nextSong(){
		stopSong();
		var nxtSong = playSong(Math.abs(++songIndex)%listLength);
		console.log("NEXT SONG : " + nxtSong );
		return nxtSong;
	}

	function previousSong(){
		stopSong();
		var prevSong = playSong(Math.abs(--songIndex)%listLength);
		console.log("Previous SONG : " + prevSong );
		return prevSong;
	}


	}
});

app.listen(port, function() {
    console.log("Server running on port " + port);
})