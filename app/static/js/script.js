function eliminaLibro(id) {
    if (confirm("Sei sicuro di voler eliminare questo libro?")) {
        fetch(`/elimina_libro/${id}`, {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                alert("Libro eliminato con successo!");
                location.reload(); // Ricarica la pagina
            } else {
                alert("Errore durante l'eliminazione del libro.");
            }
        });
    }
}

function svuotaCampi(){
    console.log("svuota campi");
    document.getElementById('new_author_nome').value = '';
    document.getElementById('new_author_cognome').value = '';
}