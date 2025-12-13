// Máscara de CPF
$(document).ready(function(){
    $('#id_cpf').mask('000.000.000-00', {reverse: true});
});

// Função para validar CPF
function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma = 0;
    if (strCPF == "00000000000") return false;
    if (strCPF == "11111111111") return false;
    if (strCPF == "22222222222") return false;
    if (strCPF == "33333333333") return false;
    if (strCPF == "44444444444") return false;
    if (strCPF == "55555555555") return false;
    if (strCPF == "66666666666") return false;
    if (strCPF == "77777777777") return false;
    if (strCPF == "88888888888") return false;
    if (strCPF == "99999999999") return false;

    for (i = 1; i <= 9; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10))) return false;

    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11))) return false;

    return true;
}

function ValidaCPF() {
    let formCpf = document.getElementById('id_cpf')
    const cpflog = document.getElementById('cpflog')
    let teste = TestaCPF(formCpf.value.replace(/[^\d]/g, ''))

    if (formCpf.value.length == 0) {
        teste = true // deixa vazio passar sem erro
        formCpf.classList.remove("is-valid", "is-invalid")
    }

    if (teste) {
        cpflog.classList.add("d-none");
        cpflog.classList.remove("d-block");
        formCpf.classList.remove("is-invalid")
        formCpf.classList.add("is-valid")
    } else {
        cpflog.classList.remove("d-none");
        cpflog.classList.add("d-block");
        formCpf.classList.remove("is-valid")
        formCpf.classList.add("is-invalid")
    }
}