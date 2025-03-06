const agregar_producto = document.getElementById('agregar')
const tabla_cuerpo = document.getElementById('tabla')
agregar_producto.addEventListener('click', function (event){ 
    event.preventDefault()

    const form = document.getElementById("form");
    const formData = new FormData(form);
    const data = {};
    const token = document.querySelector("#csrf_token").value;

    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch(CREATE_URL, {
        method: "POST",
        headers: {
            "X-CSRFToken": token,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then((res) =>
            res.json().then((json) => ({
                status: res.status,
                body: json,
            }))
        )
        .then(({ status, body }) => {
            if (status >= 400 && status <= 500) {
                console.log(body.message || "An error occurred");
            } else if (status >= 200 && status < 300) {
                console.log(status)
                console.log(body)
                console.log(body.message)
                tabla_cuerpo.insertAdjacentHTML("afterbegin", `
                     <tr id="fila_id_${body.producto.id}">
                    <th scope="row">${body.producto.nombre}</th>
                    <td>${body.producto.precio}</td>
                    <td>${body.producto.localidad}</td>
                    <td>
                        <button onClick="borrar_evento(${body.producto.id})">
                            Eliminar
                        </button>
                    </td>
                </tr>
                    `)
            }
        })
        
        .catch((error) => {
            console.log(error.message);
        });

})

function borrar_evento (id){
    const token = document.querySelector("#csrf_token").value;
    fetch(DELETE_URL, {
        method: "POST",
        headers: {
            "X-CSRFToken": token,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({"id":id}),
    })
        .then((res) =>
            res.json().then((json) => ({
                status: res.status,
                body: json,
            }))
        )
        .then(({ status, body }) => {
            if (status >= 400 && status <= 500) {
                console.log(body.message || "An error occurred");
            } else if (status >= 200 && status < 300) {
                console.log(status)
                const tabla_fila = document.getElementById(`fila_id_${id}`)
                tabla_fila.style.display="none"
                console.log(body.message)
            }
        })
        .catch((error) => {
            console.log(error.message);
        });

}