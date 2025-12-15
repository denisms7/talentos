function calcularTotalCH() {
    const cells = document.querySelectorAll('.ch-certificacao');
    let total = 0;

    cells.forEach((cell) => {
        const texto = cell.textContent.trim().replace(',', '.');

        // Aceita apenas números inteiros ou decimais
        const ehNumero = /^-?\d+(\.\d+)?$/.test(texto);

        if (ehNumero) {
            total += parseFloat(texto);
        }
    });

    document.getElementById('total-ch').textContent = total;
}

document.addEventListener('DOMContentLoaded', calcularTotalCH);