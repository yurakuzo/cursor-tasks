// Client side memory status implementation

const URL = '/stats/virtual_memory'

async function getMemoryUsage(){
    response = await fetch(URL)
    return await response.json()
}

async function generateClientHTML(){
    const memory_data = await getMemoryUsage();
    console.log(`Memory usage: ${memory_data}`)

    var span = document.getElementById('client-span')
    span.innerHTML = `${memory_data['free'] / (1024 ** 2)} / ${memory_data['total'] / (1024 ** 2)} MiB`

    var gauge_div = document.getElementById('gauge')
    gauge_div.innerHTML = `
    <div class="bar" style="background-color: rgb(72, 239, 82);
                            transform: translate(${memory_data['percent']}%);">
        <div class="data" style="display: flex;
                                justify-content: center;
                                position: absolute;
                                right: 0;
                                width: ${memory_data['percent']}%;">
            ${memory_data['percent']}%
        </div>
    </div>
    `;
}

generateClientHTML()