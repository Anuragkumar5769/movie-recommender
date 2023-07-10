var m1= film1;
var m2=film2;
var m3=film3;
var m4=film4;
var m5=film5;
var m6=film6;

  function sendData(str) {
    var data = {
        movie_name: str// Modify this value as needed
    };
    window.location.href =data.movie_name;

    // fetch('/click', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(data)
    // })
    // .then(function(response) {
    //     if (response.ok) {
    //         console.log('Success');
    //         window.location.href =data.movie_name
    //     } else {
    //         console.log('Error');
    //     }
    // })
    // .catch(function(error) {
    //     console.log(error);
    // });
}

var movie1 = document.getElementById('recommend_movies1');
movie1.addEventListener('click', function(){
    sendData(m1)
});

var movie2 = document.getElementById('recommend_movies2');
movie2.addEventListener('click', function(){
    sendData(m2)
});

var movie3 = document.getElementById('recommend_movies3');
movie3.addEventListener('click', function(){
    sendData(m3)
});

var movie4 = document.getElementById('recommend_movies4');
movie4.addEventListener('click', function(){
    sendData(m4)
});

var movie5 = document.getElementById('recommend_movies5');
movie5.addEventListener('click', function(){
    sendData(m5)
});

var movie6 = document.getElementById('recommend_movies6');
movie6.addEventListener('click', function(){
    sendData(m6)
});


