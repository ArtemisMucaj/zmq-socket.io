var socket = io();

/**
  run task
 */
 
$("#button").on('click', function(){
  // console.log("Bitch please, I just clicked the button")
  obj = {
    "socketID": socket.id,
    "content" : "example"
  };
  socket.emit('runTask', JSON.stringify(obj));
});

socket.on('getOutput', function(message){
  // console.log(message)
  $("#output").text(message)
});
