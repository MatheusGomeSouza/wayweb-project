function getAddress() {
    var postalCode = document.getElementById("postal_code")
    var address = document.getElementById("address")
    var state = document.getElementById("state")
    var city = document.getElementById("city")
    var district = document.getElementById("district")

    fetch(`https://viacep.com.br/ws/${postalCode.value}/json/`)
        .then(response => response.json())
        .then(data => {
            address.value = "logradouro" in data ? data.logradouro : ""
            state.value = "uf" in data ? data.uf : ""
            city.value = "localidade" in data ? data.localidade : ""
            district.value = "bairro" in data ? data.bairro : ""
        })
        .catch(() => {
            address.value = state.value = city.value = district.value = ""
        })
}

var maskCPF = IMask(document.getElementById('cpf'), {
    mask: '000.000.000-00'
})

var maskPostalCode = IMask(document.getElementById('postal_code'), {
    mask: '00000-000'
})