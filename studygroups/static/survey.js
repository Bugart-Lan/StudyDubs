const template = Handlebars.compile(document.querySelector('#row').innerHTML);
const arrSlotRect = [], arrSlot = []
const lengthY = 12
const COLOR = "green"
document.addEventListener('DOMContentLoaded', () => {
    create_table()
    init_arrSlot()

    var drag = false, rect1, rect2, color, prev = []
    var i1, j1
    document.querySelector('table').onmousemove = event => {
        if (!drag) return

        prev.forEach(p => {
            change(p[0], p[1])
        })
        prev = []

        const i2 = findX(event.clientX), j2 = findY(event.clientY + window.scrollY)
        for (let i = Math.min(i1, i2); i <= Math.max(i1, i2); i++)
            for (let j = Math.min(j1, j2); j <= Math.max(j1, j2); j++)
                prev.push(change(arrSlot[j][i], color))
    }

    document.querySelector('table').onmouseup = event => {
        drag = false
        prev = []
    }

    document.querySelectorAll('.slot').forEach(slot => {
        slot.onmousedown = () => {
            drag = true
            i1 = findX(event.clientX), j1 = findY(event.clientY + window.scrollY)
            if (slot.style.backgroundColor == COLOR)
                color = "white"
            else
                color = COLOR
            change(slot, color)
        }
    })
})

function create_table() {
    for (let m = 0, i = 0; m < lengthY * 30; m += 30, i++) {
        const content = template({'time': toTime(m) + ' - ' + toTime(m + 30),
                                'name1': '' + i + 0, 'name2': '' + i + 1, 'name3': '' + i + 2,
                                'name4': '' + i + 3, 'name5': '' + i + 4, 'name6': '' + i + 5,
                                'name7': '' + i + 6})
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

function init_arrSlot() {
    document.querySelectorAll('tr').forEach(tr => {
        var subarrRect = [], subarr = []
        tr.querySelectorAll('.slot').forEach(slot => {
            subarr.push(slot)
            subarrRect.push(slot.getBoundingClientRect())
        })
        arrSlot.push(subarr)
        arrSlotRect.push(subarrRect)
    })
    arrSlotRect.shift()
    arrSlot.shift()
}

function findCoordinate(x, y) {
    return arrSlotRect[findY(y)][findX(x)]
}

function findX(tarX) {
    return findXHelper(0, 7, tarX)
}

function findY(tarY) {
    return findYHelper(0, lengthY, tarY)
}

function findXHelper(a, b, tarX) {
    if (b - a <= 1)
        return a
    const i = Math.floor((a + b) / 2)
    if (tarX <= arrSlotRect[0][i].right && tarX >= arrSlotRect[0][i].left)
        return i
    else if (tarX >= arrSlotRect[0][i].right)
        return findXHelper(i + 1, b, tarX)
    else
        return findXHelper(a, i, tarX)
}

function findYHelper(a, b, tarY) {
    if (b - a <= 1)
        return a
    const i = Math.floor((a + b) / 2)
    if (tarY <= arrSlotRect[i][0].bottom && tarY >= arrSlotRect[i][0].top)
        return i
    else if (tarY >= arrSlotRect[i][0].bottom)
        return findYHelper(i + 1, b, tarY)
    else
        return findYHelper(a, i, tarY)
}

function change(slot, color) {
    const original_color = slot.style.backgroundColor
    slot.querySelector('input').value = (color == COLOR)
    slot.style.backgroundColor = color
    return [slot, original_color]
}
