const questions = [
    "Question #1",
    "Question #2",
    "Question #3",
    "Question #4",
    "Question #5",
]

const scale = 10

const template = Handlebars.compile(document.querySelector("#question").innerHTML)

document.addEventListener('DOMContentLoaded', () => {
    create_body()
})

function create_body() {
    for (let i = 0; i < questions.length; i++) {
        var content = "<h5>" + questions[i] + "</h5>"
        for (let j = 0; j < scale; j++) {
            const tmp = template({'val': j, 'name': i})
            content += tmp
        }
        document.querySelector('#survey_body').innerHTML += content
    }
}
