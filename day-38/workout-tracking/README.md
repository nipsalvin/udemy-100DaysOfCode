`GET Request`
https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts

let url = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts';
fetch(url)
.then((response) => response.json())
.then(json => {
  // Do something with the data
  console.log(json.workouts);
});

`POST Request`
https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts

let url = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts';
let body = {
workout: {
    ...
}
}
fetch(url, {
method: 'POST',
body: JSON.stringify(body)
})
.then((response) => response.json())
.then(json => {
// Do something with object
console.log(json.workout);
});

