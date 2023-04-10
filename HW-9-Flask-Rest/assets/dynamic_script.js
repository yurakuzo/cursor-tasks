const URL = '/stats/virtual_memory'

async function getMemoryUsage() {
    response = await fetch(URL)
    return await response.json()
}

async function documentUPD(data) {
    const memData = await getMemoryUsage()
    const percent = memData['percent']
    console.log(percent)

    document.getElementsByClassName('data').item('width').innerHTML = `${percent}%`
    document.querySelector('.bar').style.transform = `translate(${percent}%, 0)`

    var span = document.getElementById('dynamic-span')
    span.innerHTML = `${(memData['free'] / (1024 ** 2)).toFixed(2)} / ${(memData['total'] / (1024 ** 2)).toFixed(2)} MiB`
}

async function dynamicUPD() {
    fetch(URL)
        .then(getMemoryUsage())
        .then(documentUPD)
}

async function start() {
    setInterval(dynamicUPD, 2000)
}

start()
