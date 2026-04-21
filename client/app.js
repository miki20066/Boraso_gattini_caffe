/**
 * Invia una richiesta al backend per registrare un nuovo ordine.
 * Gestisce l'autenticazione tramite JWT e aggiorna l'interfaccia utente.
 */
async function inviaNuovoOrdine() {
    const feedbackArea = document.getElementById("result");

    try {
        // Recupero i dati dal modulo con nomi variabili personalizzati
        const idArticolo = parseInt(document.getElementById("prodotto_id").value);
        const numeroPezzi = parseInt(document.getElementById("quantita").value);

        // Costruisco l'oggetto richiesta
        const payloadOrdine = {
            note: "Ordine effettuato tramite interfaccia Boraso",
            prodotti: [
                { prodotto_id: idArticolo, quantita: numeroPezzi }
            ]
        };

        const risposta = await fetch(`${API_URL}/ordini/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}`
            },
            body: JSON.stringify(payloadOrdine)
        });

        if (!risposta.ok) {
            throw new Error(`Errore server: ${risposta.status}`);
        }

        const esito = await risposta.json();
        console.log("Dettaglio ordine salvato:", esito);

        feedbackArea.className = "success"; // Potresti usare classi CSS diverse
        feedbackArea.textContent = "Ordine inviato correttamente! 🐾";

    } catch (errore) {
        console.error("Fallimento nell'invio dell'ordine:", errore);
        feedbackArea.className = "error";
        feedbackArea.textContent = "Si è verificato un problema con l'ordine. Riprova.";
    }
}