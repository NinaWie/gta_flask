function demo_javascript_method() {
    const url = 'http://localhost:8989/access_with_javascript'
    fetch(url)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            document.getElementById("demo").innerHTML = JSON.stringify(json)
        })
}

function demo_get_ajax() {
    $.ajax({
        // URL to the Vercel production deployment (vercel --prod will give you this link)
        url: 'https://exercise-pearl.vercel.app/access_with_javascript',
        type: 'GET',
        dataType: 'JSON',
        success: function (data) { 
            console.log(data);
            document.getElementById("demo").innerHTML = JSON.stringify(data)
        },
        error: function (data) { console.log(data); },
    });
}

function demo_post_ajax() {
    var users = {
        username: "Gta_user",
        password: 1234
      };
    $.ajax({
        // URL to the Vercel production deployment (vercel --prod will give you this link)
        url: 'https://exercise-pearl.vercel.app/using_post',
        type: 'POST',
        dataType: 'JSON',
        data: JSON.stringify(users),
        success: function (data) { console.log(data);},
        error: function (data) { console.log(data); },
    });
}

// TODO TASK 4 - call Python backend for decreasing or increasing the value
function decrease_value() {
    const url = 'http://localhost:8989/decrease_value'
    fetch(url)
        .then(response_sub => response_sub.json())
        .then(json => {
            console.log(json);
            minus_num= json - 1
            document.getElementById("sub").innerHTML = JSON.stringify(minus_num)
        })
}

function increase_value() {
    const url = 'http://localhost:8989/increase_value'
    fetch(url)
        .then(response_add => response_add.json())
        .then(json => {
            console.log(json);
            add_num = json + 1
            document.getElementById("add").innerHTML = JSON.stringify(add_num)
        })
}