const template = Handlebars.compile(document.querySelector('#row').innerHTML);

const lengthX = 7
const lengthY = 12

document.addEventListener('DOMContentLoaded', () => {
    create_table();
    console.log(ctime)
})

function create_table() {
    for (let m = 0, i = 0; m < lengthY * 30; m += 30, i++) {
        const colors = []
        for (let j = 0; j < lengthX; j++) {
            if (ctime[j][i])
                colors.push("green")
            else
                colors.push("white")
        }
        const content = template({'time': toTime(m) + ' - ' + toTime(m + 30), 'c1': colors[0],
                                'c2': colors[1], 'c3': colors[2], 'c4': colors[3], 'c5': colors[4],
                                'c6': colors[5], 'c7': colors[6]})
        document.querySelector('#schedule-row').innerHTML += content
    }
}

function toTime(mins) {
    return formatTwoDigits(mins / 60) + ":" + formatTwoDigits(mins % 60)
}

function formatTwoDigits(n) {
    if (Math.floor(n / 10) == 0)
        return "0" + Math.floor(n)
    else
        return Math.floor(n)
}
