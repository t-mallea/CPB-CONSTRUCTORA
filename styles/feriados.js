

let url = "https://apis.digital.gob.cl/fl/feriados"
$.get(url, function(respuesta){

    console.log(respuesta)

}, "json")